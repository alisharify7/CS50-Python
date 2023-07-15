import re
import sys


def main():
    print(count(input("Text: ")))
    sys.exit(0)

def count(s):
    # s = s.lower()
    ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(ums)


if __name__ == "__main__":
    main()