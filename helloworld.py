import sys

def main():
    print(f"Hello World! From Python: {str(sys.version_info)}")
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        raise Exception('Python version 3.6.x is unsupported!')


if __name__ == "__main__":
    main()
