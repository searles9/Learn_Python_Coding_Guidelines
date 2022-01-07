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