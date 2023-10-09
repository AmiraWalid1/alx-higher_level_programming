#!/usr/bin/python3
import sys


def main():
    argv_len = len(sys.argv) - 1
    print('{:d}'.format(argv_len),
          ('argument' if argv_len == 1 else 'arguments') +
          ('.' if argv_len == 0 else ':'))
    for i in range(1, argv_len + 1):
        print('{}: {}'.format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
