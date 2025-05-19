import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    #forgot to add \b at the beginning and end of the regex
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    
    # Return the number of matches found
    return len(matches)


if __name__ == "__main__":
    main()