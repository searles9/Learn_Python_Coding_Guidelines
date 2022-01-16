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
number_1(folder)
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