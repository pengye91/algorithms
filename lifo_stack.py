#!/usr/bin/env python
# encoding: utf-8


class Stack():
    inner_list = []
    numbers = 0
    def __init__(self):
        self.inner_list = []
        self.numbers = 0
    
    def push(self, item):
        self.inner_list.append(item)
        self.numbers = self.numbers + 1
    
    def pop(self):
        try:
            self.numbers -= 1
            return self.inner_list.pop()
        except IndexError as e:
            raise e
    
    def is_empty(self):
        return self.numbers == 0
    
    def peek(self):
        return self.inner_list[self.numbers - 1]
    
    def __next__(self):
        if self.numbers == 0:
            raise StopIteration
        self.numbers -= 1
        return self.inner_list[self.numbers]

    def __iter__(self):
        return self
    
    def __repr__(self):
        return str(self.inner_list)
        