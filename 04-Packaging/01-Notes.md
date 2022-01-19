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
* you can generate html docs based on your code: https://www.mkdocs.org/
* it is common to put them in a docs folder
* mkdocs works with certian type of docstrings - the best option is probably to use the google-style docstrings
1. you create the markdown files
2. you can specify what docstrings should be converted to html documentation (google docstrings in this case)
   1. ex: 
   ```
   # References

   ## Vector Class
   ::: fastvector.vector
   ```
   2. this will generate documentation for every function in the vector.py file
3. you can make an ```mkdocs.yaml``` file which contains the configuration for the documentation
4. you can see all the possible commands ... ```mkdocs --help```
5. to generate the HTML file run ```mkdocs build```
   1. it will generate the docs in the "site" directory
6. you can run ```mkdocs serve``` which rull run the site on your local machine 
***
***
# Install Make and Git
```
    Mac:
    Brew: https://brew.sh/index_de
    Git: brew install git
    Make: brew install make

    Debian Linux:
    Git: sudo apt-get install git
    Make: sudo apt-get install make

    Windows:
    Chocolatey: https://chocolatey.org/install
    Git: choco install git
    Make: choco install make
```
***
***
# Github Repository and GitHub Pages
* you can make a github repo and setup CI/CD and make it easy to see the docs
1. create a public repo 
2. git init in the project folder
3. git add .
4. git commit -m "message"
5. git branch -M main
6. git push -u origin main
7. activate your virtual enviorment
8. mkdocs --help
9. deploy the docs to GHE: mkdocs gh-deploy
   1.  this creates a new github branch called github-pages
   2.  you can click enviorments and it will show the docs
***
***
# Makefile and Requirements
* the requirements.txt file contains the pip packages that your program needs to run
* you may also want to make a requirements-dev.txt file that contains all the pip packages that the developers need to develop the code
* the setup.py file also contains the required packages and those packages will be installed when you run the file
  * the requirements.txt file is different though and is for people who are downloading your code from github and need to install the packages
```
pip install -r requirements.txt
```
### Makefile
* make is a tool that uses make files
* its a way to run CLI commands easily with aliases
* you may have an alias called ```test``` that runs tests for a certian folder: ```make test```
* you may have an alias that copies files to a certian folder 
```
SRC_CORE=fastvector
SRC_TEST=tests
SRC_BENCHMARK=benchmarks

PYTHON=python
PIP=pip

help:
	@echo "Available Commands:"
	@echo " tests                  - Run unit tests."
	@echo " tests-coverage         - Run unit tests and code coverage."
	@echo " tests-coverage-html    - Run unit tests, code coverage and generate html."

test:
	$(PYTHON) -m pytest $(SRC_TEST)

test-coverage:
	$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST)
	$(PYTHON) -m codecov

test-coverage-html:
	$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST) --cov-report=html
```
***
***
# More to Unit-Tests
* example piece of test code:
```
class VectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v1 = Vector2D(0, 0)
        self.v2 = Vector2D(-1, 1)
        self.v3 = Vector2D(2.5, -2.5)

    def test_init(self) -> None:
        result = Vector2D(-1, 1)
        self.assertEqual(result, self.v2)
        self.assertRaises(TypeError, Vector2D, 0, 'a')
        self.assertRaises(TypeError, Vector2D, 'B', 1)
        self.assertRaises(TypeError, Vector2D, 'B', 1)
```
* notice the method name ```test_```item - useful naming convention
* you can check if a function returns an exception with self.assertRaises()
***
***
# Python Test Explorer
* test explorer is a vs-code extension
* open command pallete and type Python: configure tests - configure the settings
* you can run tests easily from the test explorer
* you can run all tests or you can run a test for 1 method
* the test explorer also makes it easy to debug 
***
***
# Code Coverage 
* ```pip install pytest-cov```
* ```pip install codecov```
* you can run code coverage tools to see how much of your code has been tested
* if not 100% of your code has been tested you can add more tests
* here is an example from a makefile
```
test-coverage:
	$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST)
	$(PYTHON) -m codecov

test-coverage-html:
	$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST) --cov-report=html
```
* there is also a cloud option where everyone can see the coverage: https://about.codecov.io/
***
***
# GitHub WorkFlows and Pre-Commit
* https://pre-commit.com/
* from the website: "Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks."
* example before someone commits somthing to GHE you may want to use pre-commit to run flake8 and autopep
* example pre-commit.yaml file:
```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-docstring-first
    -   id: check-yaml

-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.4
    hooks:
    -   id: flake8

-   repo: https://github.com/pre-commit/mirrors-autopep8
    rev: v1.5.4
    hooks:
    -   id: autopep8

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.790
    hooks:
    -   id: mypy

-   repo: https://github.com/PyCQA/isort
    rev: 5.7.0
    hooks:
    -   id: isort
```
* parts explained:
  * repo: the repo or package to use for the hoop
  * rev: the version of the package
    * go to the repo and check the releases portion to see the versions
  * hooks: the name of the item
* to setup precommit use ```pre-commit install```
* to run it on your own: ```pre-commit run --all-files```
### CI tests
* you can run continous integration tests in github
* you would need to make a workflows folder  - under this path: ```.github\workflows```
* see the section code for an example (section-code\example_github_code\FastvectorEng\.github\workflows)