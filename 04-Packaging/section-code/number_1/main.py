# main.py

from package_1.printing import print_hello_world
from package_1.printing import print_name

def main() -> None:
    print_hello_world()
    print_name("Donovan")

if __name__ == "__main__":
    main()
