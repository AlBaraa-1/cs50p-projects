import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    segment = r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    return bool(re.fullmatch(segment, ip))


if __name__ == "__main__":
    main()
