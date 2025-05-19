import re
import sys


def main():
    # parse the input from the user and print the result
    print(parse(input("HTML: ")))


def parse(s):
    # regex to match the YouTube URL in the HTML string
    url = r"^<iframe\ssrc=\"https?://(?:www\.)?youtube\.com/embed/([\w-]+)\"></iframe>$"

    # search for the URL in the input string
    src = re.search(url, s)
    if src:
        # return the YouTube URL in the format "https://youtu.be/VIDEO_ID"
        return "https://youtu.be/" + src.group(1)


if __name__ == "__main__":
    main()