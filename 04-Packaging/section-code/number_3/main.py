# main.py - package 2

from package_3.utils.printing import print_hello_world
from package_3.utils.printing import print_name

def main() -> None:
    print_hello_world()
    print_name("Donovan")

if __name__ == "__main__":
    main()
