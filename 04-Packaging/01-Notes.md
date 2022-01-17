***
# Packaging 
***
***
# Modules and Packages - Part 1
* ```__init__.py``` tells Python that it is a package
* see the ```number_1``` folder in the section code folder
```
number_1(folder)
---package_1(folder/package)
------__init__.py (part of the package)
------printing.py (part of the package)
---main.py (not part of package)
```
```
from package_1.printing import print_hello_world
from package_1.printing import print_name
```
***
* you can also make sub directories for a package:
```
number_2(folder)
---package_2(folder/package)
------__init__.py (tells python that its a package)
------utils(folder-sub-package)
---------__init__.py (part of the sub-package)
---------printing.py (part of the sub-package)
---main.py (not part of package)
```
```
from package_2.utils.printing import print_hello_world
from package_2.utils.printing import print_name
```
***
* some important notes:
* any python file is a python module
* a python package is a directory structure where you have several python files defined. You can also have subdirectories where more Python files are defined
***
***
# Modules and Packages - Part 2
```
number_3(folder)
---package_3(folder/package)
------__init__.py (tells python that its a package)
------utils(folder-sub-package)
---------printing (sub package of sub package)
------------printing.py (part of the printing sub-package)
------------__init__.py (part of the printing sub-package)
---------__init__.py (part of the sub-package)
---main.py (not part of package)
```
* you can make sub packages withing sub packages
* you can control what people can import from the packages
* for example you could add this to the ```__init__.py``` printing sub package:
```
from ._printing import print_hello_world
from ._printing import print_name

# you can list all functions that you want to export to the outside:
__all__ = [
    "print_hello_world",
    "print_name"
]
```
* in the main.py file you can then import them the same way:
```
from package_3.utils.printing import print_hello_world
from package_3.utils.printing import print_name

# or you can do this which would 
# import everything in the __all__ list - IT HAS TO BE IN THAT # LIST IN THE __init__.py file:
from package_3.utils.printing import *
```
* it is discouraged to use wildcard imports because you dont have a clear idea of what you are importing 
* linting tools also have problems with the wildcard imports
***
***
# Creating a Package for an Example Vector Class
* view the ```example_vector``` folder
* notice the imports in the ```__init__.py``` files
* notice how the unit test folder also has a ```__init__.py``` file
* there is also a setup.py file
  * this file allows you to configure the different attributes of the python package
  * ```from setuptools import setup```
  * versions: major.minor.micro (example: 1.4.0)
  * micro: bug fixes that dont add any new functionality
  * minor: adding new functions without changing the existing code
  * major: breaking changes that will change the whole behavior of the package 
* ```python setup.py install``` will install your final python package version to your Python enviorment 
* ```python setup.py develop``` will install the current version (local files) which is in development
***
***
# HTML Documentation with Mkdocs
*