***
# Debugging, Unit-Testing and Timing
***
***
# Debugging in VS Code
* click run an debug from the left bar
* click run and debug
* click debug the current active python file
* if things fail Python will show you where it is failing
* you can choose - continue, step over, skip from the slider bar that pops up
* step into: it lets you check under the hood - it will take you to the function where the code is being run from - like a class method or function 
* step over - skip one line
* you can click the debug console from the terminal and run python commands there
* before you make corrections it can be helpful to run the commands in the debug console
* you can create a launch.json file to keep the debugging settings - that way you dont have to specify them everytime you run debug
* callstack - specifies what functions were called - a func called b func
* in the watch section you can enter certian values to see what they evaulate too - myvar1 + myvar2
* the variables tab shows all the local variables
***
***
# Timing 
* docs: https://docs.python.org/3/library/timeit.html
* example:
```
from timeit import Timer
import numpy as np

NUM_RUNS = 3

def test_addition_standard_bib() -> None:
    code_str = (
'''
v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
v3 = v1 + v2
'''
    )
    import_str = (
'''
import random
from vector import Vector2D
'''
    )
    timer = Timer(code_str, setup=import_str)
    times = timer.repeat(repeat=NUM_RUNS, number=1)
    times = [t * 1_000_000_000.0 for t in times]
    mean_time = np.mean(times)
    print(f'Times: {times}, Mean computation time: {mean_time}')
```
* notice how the code is sotred in a string
* notice how there is no indentaion when the code is put into a string
***
***
# Profiling 
* docs: https://docs.python.org/3/library/profile.html
*  A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
*  The profiler modules are designed to provide an execution profile for a given program, not for benchmarking purposes (for that, there is timeit for reasonably accurate results). This particularly applies to benchmarking Python code against C code: the profilers introduce overhead for Python code, but not for C-level functions, and so the C code would seem faster than any Python one.
*  It can help you find bottle necks in your programs
*  example code (profiling code in another file):
```
'''Test code.
'''
# pylint: disable=import-error
import cProfile
import io
import pstats
import random
import sys
from functools import wraps

from Chapter3_CodeTesting.Profiling.vector import Vector2D


def profile(fn):
    @wraps(fn)
    def profiler(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        fn_result = fn(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        ps = pstats.Stats(profiler, stream=stream).sort_stats('time')
        ps.print_stats()
        print(stream.getvalue())
        return fn_result
    return profiler


@profile
def test_addition_own_implementation():
    for _ in range(100_000):
        v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v3 = v1 + v2  # noqa


def main() -> int:
    test_addition_own_implementation()
    return sys.exit(0)


if __name__ == '__main__':
    main()
```
* it will show the total time for a specific function call
* to measure the execution time use the timeit module <--- usually more important
* to find bottlenecks use profiles
***
***
# Unit-Testing
* docs: https://docs.python.org/3/library/unittest.html
* * there is also pytest: https://docs.pytest.org/en/6.2.x/contents.html
* the pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
* example tests:
```
'''Test code.
'''
# pylint: disable=import-error
import unittest

from Chapter3_CodeTesting.UnitTesting.vector import Vector2D


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector2D(0, 0)
        self.v2 = Vector2D(-1, 1)
        self.v3 = Vector2D(2.5, -2.5)

    def test_equality(self):
        ''' Tests the equality operator.
        '''
        self.assertNotEqual(self.v1, self.v2)
        expected_result = Vector2D(-1, 1)
        self.assertEqual(self.v2, expected_result)

    def test_add(self):
        ''' Tests the addition operator.
        '''
        result = self.v1 + self.v2
        expected_result = Vector2D(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self):
        ''' Tests the subtraction operator.
        '''
        result = self.v2 - self.v3
        expected_result = Vector2D(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self):
        ''' Tests the multiplication operator.
        '''
        result1 = self.v1 * 5
        expected_result1 = Vector2D(0.0, 0.0)
        self.assertEqual(result1, expected_result1)
        result2 = self.v1 * self.v2
        expected_result2 = 0.0
        self.assertEqual(result2, expected_result2)

    def test_div(self):
        ''' Tests the multiplication operator.
        '''
        result = self.v3 / 5
        expected_result = Vector2D(0.5, -0.5)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
```