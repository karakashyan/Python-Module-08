import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_python_path() -> str:
    return sys.executable


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def get_venv_path() -> str:
    return sys.prefix


def get_packages_path() -> str:
    return site.getsitepackages()[0]


def main() -> None:
    if is_virtual_env():
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {get_python_path()}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {get_venv_path()}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(get_packages_path())
    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {get_python_path()}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python3 -m venv --without-pip matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
