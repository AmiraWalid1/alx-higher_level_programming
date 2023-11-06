#!/usr/bin/python3
''' This Module contain MyList class '''


class MyList(list):
    ''' Class that inherits from list'''

    def print_sorted(self):
        ''' prints the list, but sorted (ascending sort) '''
        print(sorted(self))
