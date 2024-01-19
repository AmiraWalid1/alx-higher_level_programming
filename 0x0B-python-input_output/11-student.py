#!/usr/bin/python3
''' This Module contain Student Class '''


class Student:
    ''' Student calss '''
    def __init__(self, first_name, last_name, age):
        ''' init of Student calss '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Method that retrieves a dictionary representation of a Student instance
        - If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.
        - Otherwise, all attributes must be retrieved
        '''
        if isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if isinstance(attr, str) and (attr in self.__dict__.keys()):
                    new_dict[attr] = self.__dict__[attr]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        for key in self.__dict__.keys():
            if key in json.keys():
                self.__dict__[key] = json[key]
