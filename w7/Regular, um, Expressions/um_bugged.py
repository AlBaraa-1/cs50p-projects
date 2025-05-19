import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # eg: forgot to add \b
    matches = re.findall(r"um\b", s, re.IGNORECASE)

    # Return the number of matches found
    return len(matches)


if __name__ == "__main__":
    main()