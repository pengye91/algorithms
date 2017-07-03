
class LinkedNodes():

    __first__ = None
    __numbers__ = 0

    class Node():
        item = None
        nxt = None

        def __init__(self):
            self.item = None
            self.nxt = None

        def __repr__(self):
            return str(self.item)

    def __init__(self):
        self.__first__ = self.Node()

    def push(self, item):
        self.__numbers__ += 1
        __old_first__ = self.__first__
        self.__first__ = self.Node()
        self.__first__.item, self.__first__.nxt = item, __old_first__

    def pop(self):
        self.__numbers__ -= 1
        __ret__ = self.__first__.item
        self.__first__ = self.__first__.nxt
        return __ret__

    def is_empty(self):
        return self.__first__ == None

    def size(self):
        return self.__numbers__

    def __repr__(self):
        __temp__ = self.__first__
        __representation__ = str(__temp__.item)
        while(__temp__.nxt):
            if __temp__.nxt.item:
                __representation__ += '-->'
                __representation__ += str(__temp__.nxt.item)
            __temp__ = __temp__.nxt
        return __representation__
