#!/usr/bin/python3
def uppercase(str):
    upper_str = ''
    for ch in str:
        if ord('z') >= ord(ch) >= ord('a'):
            upper_str += chr(ord(ch)-32)
        else:
            upper_str += ch
    print('{}'.format(upper_str))
