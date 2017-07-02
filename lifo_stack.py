#!/usr/bin/env python
# encoding: utf-8


class Stack():
    __inner_list__ = []
    __numbers__ = 0

    def __init__(self):
        self.__inner_list__ = []
        self.__numbers__ = 0

    def push(self, item):
        self.__inner_list__.append(item)
        self.__numbers__ = self.__numbers__ + 1

    def pop(self):
        try:
            self.__numbers__ -= 1
            return self.__inner_list__.pop()
        except IndexError as e:
            raise e

    def is_empty(self):
        return self.__numbers__ == 0

    def peek(self):
        return self.__inner_list__[self.__numbers__ - 1]

    def __next__(self):
        if self.__numbers__ == 0:
            raise StopIteration
        self.__numbers__ -= 1
        return self.__inner_list__[self.__numbers__]

    def __iter__(self):
        self.__numbers__ = len(self.__inner_list__)
        return self

    def __repr__(self):
        return str(self.__inner_list__)

