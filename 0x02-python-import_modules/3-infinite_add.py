#!/usr/bin/python3
import sys


def infinite_add():
    print(sum(int(num) for num in sys.argv[1:]))


if __name__ == "__main__":
    infinite_add()
