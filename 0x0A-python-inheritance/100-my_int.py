#!/usr/bin/python3
'''This module contain:
MyInt class - inherits from int.
'''


class MyInt(int):
    ''' class MyInt that inherits from int '''
    def __eq__(self, other):
        '''return __ne__'''
        return super().__ne__(other)

    def __ne__(self, other):
        '''return __eq__ '''
        return super().__eq__(other)
