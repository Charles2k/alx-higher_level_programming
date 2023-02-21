#!/usr/bin/python3
"""Makes a single link list"""


class Node:
    """Defines Node class"""
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
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines Single Linked List"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        temp = self.__head
        if temp.data > value:
            new.next_node = temp
            self.__head = new
            return

        while temp.next_node:
            if temp.next_node.data > value:
                break
            temp = temp.next_node

        new.next_node = temp.next_node
        temp.next_node = new

    def __str__(self):
        llist = []
        temp = self.__head
        while temp is not None:
            llist.append(temp.data)
            temp = temp.next_node
        return "%s" % ('\n'.join(str(i) for i in llist))
