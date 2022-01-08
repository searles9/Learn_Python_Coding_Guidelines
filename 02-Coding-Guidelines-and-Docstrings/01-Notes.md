***
# Coding Guidelines and Docstrings
***
***
# PEP 8 Coding Guidelines - Part 1
* This is the full PEP 8 style guide: https://www.python.org/dev/peps/pep-0008/ 
  * Imports: https://www.python.org/dev/peps/pep-0008/#imports 
    * imports should be on seperate lines
    * Imports should be grouped in the following order:
      1. Standard library imports.
      2. Related third party imports.
      3. Local application/library specific imports.
  * Indentation: https://www.python.org/dev/peps/pep-0008/#indentation 
    * use 4 spaces
  * Comments: https://www.python.org/dev/peps/pep-0008/#comments  
  * Naming Convention: https://www.python.org/dev/peps/pep-0008/#naming-conventions  
  * Programming Recommendations: https://www.python.org/dev/peps/pep-0008/#id51  
***
***
# PEP 8 Coding Guidelines - Part 2
* example of properly formated code:
```
import sys #  build in imports

import numpy as np #  third part packages
import pandas as pd

from .my_lib import print_hello #  custom modules


def my_function_with_many_params(
    param1,
    param2,
    param3,
    param4
):
    return "Hello World!"


user1 = "Jan"
user2 = "Max"
user3 = "Marcus"

my_list = [
    user1,
    user2,
    user3
]


if __name__ == "__main__":
    print_hello()
```
***
***
# Code Linter - Pylint - Part 1
```
pip install pylint
pip install pylint --upgrade
```
```
pylint test_pylint.py
```
* Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code's complexity.
***
***
# Code Linter - Pylint - Part 2
* pylint guide: https://pylint.pycqa.org/en/latest/
```
pylint --help
```
* you can make a pylint configuration file (this specific one should go in the same folder as the file you are testing)
```
pylint --generate-rcfile > .pylintrc
```
* you need to create a different file based on where the files you are testing are - see [command line options](https://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options)
* here are some of the important parts of the pylint file:
  * you can disable some of the warnings - either by the name or code of the warning (name is easier)
  * ex error: C0303: Trailing whitespace
  ```
  disable=print-statement
  # User-defined
  trailing-whitespace,
  missing-module-docstring,
  missing-class-docstring,
  C0103
  ```
  * you can also add a comment directly to the file set pylint settings
  ```
  # pylint: disable=invalid-name
  ```
***
***
# Code Linter - Flake8
* flake8 guide: https://flake8.pycqa.org/en/latest/
* flake8 focuses heavily on checking if the code follows the PEP8 guidleines (more than pylint)
```
python3 -m pip install flake8
```
* to run flake8:
```
flake8 path/to/code/code.py
```
* you can make a config file:
```
touch .flake8
```
* see the flake 8 guide for info on how the config file should look
* here is an example: 
```
[flake8]
ignore = W291,F501
exclude =
    .git,
    __pycache__,
    docs/source/conf.py,
    old,
    build,
    dist
max-complexity = 10
```
* view the flake8 guide to see the errors and warnings that exist
* flake8 is faster than pylint because it checks the code on a higher level 
***
***
# Tool - isort
* isort will automatically order your imports
* docs: https://pycqa.github.io/isort/
```
pip install isort
```
* usage:
```
isort yourpythonfile1.py yourpythonfile2.py

# recursivley - basically isort **/*.py 
isort . 

# see the proposed changes without applying them
isort file.py --diff

# apply changes only if they dont introduce syntax errors
isort --atomic
```
* you can make a configuration file:
```
touch .isort.cfg
```
* example config file:
```
# .isort.cfg
[settings]

# Maximum length (columns) for a line of program code.
line_length = 80

# Number of blank lines to separate imports from following statements.
lines_after_imports = 2

# Names of sections that group import statements.
# The order in this sequence specifies the order the sections should appear.
sections =
    FUTURE
    STDLIB
    THIRDPARTY
    FIRSTPARTY
    LOCALFOLDER

# Name of section for any import statement of a package not known to ‘isort’.
default_section = LOCALFOLDER

# Package names that are known for the ‘THIRDPARTY’ section.
known_third_party = numpy,pandas,keras,tensorflow,sciypy,sklearn,pylint

# Package names that are known for the ‘FIRSTPARTY’ section.
known_first_party =

# The multi-line import statement style (integer code).
# See the ‘isort’ documentation for the meaning of each code.
multi_line_output = 3

force_single_line = True
```
***
***
# Formater - Autopep8
* autopep8 docs: https://pypi.org/project/autopep8/
* autopep 8 allows you to create a configuration file
* usage - the file will be modified after running this:
```
autopep8 file.py
```
* if you just want to see the differences:
```
autopep8 file.py --diff
```
* more usage:
```
# this will modify the python file in place:

autopep8 file.py --in-place
```
* the .flake8 config file controls what autopep8 AND flake 8 check for 
***
***
# Formater - Black
* black is a bit agressive and is not very configurable 
* https://black.readthedocs.io/en/stable/
* https://github.com/psf/black
```
pip install black
```
* usage:
```
# see proposed changes
black file.py --diff
```
* this might not be a great tool for existing code bases - autopep8 might be a better option 
***
***
# Docstring - Numpy Style
* doc string - "documentation strings"
### python docstring generator
* you can use the "python docstring generator" extension to easily make extensions
1. click settings, settings again
2. click extensions, click the "python docstring generator" extension
3. you can specify what docstring style to use 
4. you can optionaly enable "generate docstring on enter"
5. create a python function and start a docstring - choose generate docstring
* example:
```
     def __init__(self, x=0, y=0):
        '''[summary]

        Parameters
        ----------
        x : int, optional
            [description], by default 0
        y : int, optional
            [description], by default 0

        Raises
        ------
        TypeError
            [description]
        '''
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')
```
* example with filled in values:
```
    def __init__(self, x=0, y=0):
        '''Create a vector 2d object.

        Parameters
        ----------
        x : int, optional
            The X coorinate of the 2d vector, by default 0
        y : int, optional
            The y coorinate of the 2d vector, by default 0

        Raises
        ------
        TypeError
            You must pass in int/float values for x and y!
        '''
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')
```
***
***
# Docstring - ReST (Sphinx)
* example: 
```
    def __init__(self, x=0, y=0):
        '''[summary]

        :param x: [description], defaults to 0
        :type x: int, optional
        :param y: [description], defaults to 0
        :type y: int, optional
        :raises TypeError: [description]
        '''
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')
```
***
***
# Docstring - Google style
* example:
```
'''[summary]

        Args:
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.

        Raises:
            TypeError: [description]
        '''
```
* this style can be easily parsed to generate HTML documentation 
***
***
# Code linter - Pydocstyle 
* docs: https://www.pydocstyle.org/en/stable/
* this tool checks compliance with Python docstring conventions 
```
pip install pydocstyle
```
* run for google doc strings
```
# this will output the issues
pydocstyle --convention=google file.py
```
* you can add a configuration file to configure things
```
touch .pydocstyle
```
* example config file:
```
[pydocstyle]
inherit = false
ignore = D100,D203,D405
match = .*\.py
```
***
***
# Type Annotations and Mypy - Part 1
* type annotations are a way of showing what type a variable or paramater should be
* its documentation and not so much a restriction 
* docs: https://docs.python.org/3/library/typing.html
* ex: 
```
def greeting(name: str) -> str:
    return 'Hello ' + name
```
* ex 2: 
```
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```
### large example:
```
'''Own implementation of a 2D vector class.
'''
from __future__ import annotations

import numbers
from functools import total_ordering
from math import sqrt
from typing import SupportsFloat
from typing import Union


@total_ordering
class Vector2D:
    '''Vector2D class to perform simple vector operations.
    '''

    def __init__(self, x: SupportsFloat = 0, y: SupportsFloat = 0) -> None:
        '''Create a vector instance with the given x and y values.

        Args:
            x (SupportsFloat, optional): x-Value. Defaults to 0.
            y (SupportsFloat, optional): y-Value. Defaults to 0.

        Raises:
            TypeError: If x or y are not a number.
        '''
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')

    def __call__(self) -> str:
        '''Callable for the vector instance representation.

        Returns:
            str: The representation of the vector instance.
        '''
        print('Calling the __call__ function!')
        return self.__repr__()

    def __repr__(self) -> str:
        '''Return the vector instance representation.

        Returns:
            str: The representation of the vector instance.
        '''
        return f'vector.Vector2D({self.x}, {self.y})'

    def __str__(self) -> str:
        '''The vector instance as a string.

        Returns:
            str: The vector instance as a string.
        '''
        return f'({self.x}, {self.y})'

    def __bool__(self) -> bool:
        '''Return the truth value of the vector instance.

        Returns:
            bool: True, if the vector is not the Null-vector. False, else.
        '''
        return bool(abs(self))

    def __abs__(self) -> float:
        '''Return the length (magnitude) of the vector instance.

        Returns:
            float: Length of the vector instance.
        '''
        return sqrt(self.x**2.0 + self.y**2.0)

    def check_vector_types(self, vector: object) -> None:
        '''Check if the vector is an instance of the Vector2D class.

        Args:
            vector (object): A vector instance.

        Raises:
            TypeError: If vector is not an instance of the Vector2D class.
        '''
        if not isinstance(self, Vector2D) or not isinstance(vector, Vector2D):
            raise TypeError('You have to pass in two instances of the vector class!')

    def __eq__(self, other_vector: object) -> bool:
        '''Check if the vector instances have the same values.

        Args:
            other_vector (object): Other vector instance (right-hand-side of the operator)

        Returns:
            bool: True, if the both vector instances have the same values. False, else.
        '''
        self.check_vector_types(other_vector)
        is_equal = False
        if isinstance(other_vector, Vector2D):
            if self.x == other_vector.x and self.y == other_vector.y:
                is_equal = True
        return is_equal

    def __lt__(self, other_vector: Vector2D) -> bool:
        '''Check if the self instance is less than the other vector instance.

        Args:
            other_vector (Vector2D): Other vector instance (right-hand-side of the operator).

        Returns:
            bool: True, if the self instance is less than the other vector instance. False, else.
        '''
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        '''Returns the additon vector of the self and the other vector instance.

        Args:
            other_vector (Vector2D): Other vector instance (right-hand-side of the operator).

        Returns:
            Vector2D: The additon vector of the self and the other vector instance.
        '''
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        '''Return the subtraction vector of the self and the other vector instance.

        Args:
            other_vector (Vector2D): Other vector instance (right-hand-side of the operator).

        Returns:
            Vector2D: The subtraction vector of the self and the other vector instance.
        '''
        self.check_vector_types(other_vector)
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other: Union[SupportsFloat, Vector2D]) -> Union[SupportsFloat, Vector2D]:
        '''Return the multiplication of the self vector and the other vector(or number) instance.

        Args:
            other (Union[SupportsFloat, Vector2D]): Other vector instance or scaler
                value (right-hand-side of the operator)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            Union[SupportsFloat, Vector2D]: The multiplication of the self vector and the other
                vector(or number) instance.
        '''
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, numbers.Real):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError('You must pass in a vector instance or an int/float number!')

    def __truediv__(self, other: SupportsFloat) -> Vector2D:
        '''Return the multiplication of the self vector and the other vector(or number) instance.

        Args:
            other: Other vector instance or scaler value (right-hand-side of the operator).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            SupportsFloat: The multiplication of the self vector and the other vector(or number) instance.
        '''
        if isinstance(other, numbers.Real):
            if other != 0.0:
                return Vector2D(self.x / other, self.y / other)
            else:
                raise ValueError('You cannot divide by zero!')
        else:
            raise TypeError('You must pass in an int/float value!')

```
* if you run mypy file.py and it find errors it will show the errors 
  *  for example you might specify a int return type but will get an error if you are returning a float 
* you can specify a union - which is basically a list of types that are allowed ... ```Union[SupportsFloat, Vector2D]```
***
***
# Type Annotations and Mypy - Part 2