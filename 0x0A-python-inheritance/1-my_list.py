#!/usr/bin/python3
''' This Module contain MyList class '''


class MyList(list):
    ''' define MyList class '''

    def print_sorted(self):
        ''' prints the list, but sorted (ascending sort) '''
        print(sorted(self))
