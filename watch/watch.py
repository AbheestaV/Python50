import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = "https://youtu.be/"
    if matches := re.search(r'^<iframe.+src="https?://(?:www\.)?youtube\.com/embed/(\w+).+></iframe>$', s.strip()):
        url += matches.group(1)
        return url




if __name__ == "__main__":
    main()
