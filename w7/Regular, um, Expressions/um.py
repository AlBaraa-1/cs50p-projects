import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Use regex to find all case-insensitive, whole-word matches of "um"
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    # Return the number of matches found
    return len(matches)


if __name__ == "__main__":
    main()