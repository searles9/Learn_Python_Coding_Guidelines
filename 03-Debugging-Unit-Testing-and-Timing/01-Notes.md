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