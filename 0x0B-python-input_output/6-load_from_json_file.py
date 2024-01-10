#!/usr/bin/python3
'''this module contain Save load_from_json_file function'''
import json


def load_from_json_file(filename):
    '''
    function that creates an Object from a “JSON file”
    '''
    with open(filename, 'r') as f:
        return json.load(f)
