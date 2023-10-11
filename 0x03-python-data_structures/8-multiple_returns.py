#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), None if not len(sentence) else sentence[0])
