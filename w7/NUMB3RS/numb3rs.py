import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Each segment of the IP address (0-255)
    segment = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"

    # Full regex pattern for IPv4
    pattern = rf"^{segment}\.{segment}\.{segment}\.{segment}$"

    # Match against the pattern
    if re.fullmatch(pattern, ip):
        return True
    else:
        return False



if __name__ == "__main__":
    main()