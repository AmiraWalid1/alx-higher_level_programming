#!/usr/bin/python3
"""
100-singly_linked_list.py:  defines class node of a singly linked list
and class SinglyLinkedList
"""


class Node:
    """class Node defined"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList defined"""
    def __init__(self):
        self.__head = None

    def __str__(self) -> str:
        values = []
        curr = self.__head
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        curr = self.__head
        prev_node = None
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        while curr is not None:
            if value < curr.data:
                new_node.next_node = curr
                if prev_node is not None:
                    prev_node.next_node = new_node
                return
            prev_node = curr
            curr = curr.next_node
        prev_node.next_node = new_node
