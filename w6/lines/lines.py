import sys


def main():
    root = get_route()
    count = count_lines(root)
    print(count)

def count_lines(file):
    count = 0
    with open(file) as file:
        for line in file:
            line = line.strip()
            if not line.startswith("#") and line != "":
                count += 1
    return count


def get_route():
    # expecting one command line argument
    if len(sys.argv) == 2:
        pass
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

    # check ends with .py
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # check if file exists
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")

    return sys.argv[1]


if __name__ == "__main__":
    main()
