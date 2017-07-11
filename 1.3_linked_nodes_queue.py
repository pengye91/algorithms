class LinkedNodesQueue():
    __first__ = None
    __last__ = None
    __numbers__ = 0

    class Node():
        item = None
        nxt = None

        def __init__(self):
            self.item = None
            self.nxt = None
        
    def __init__(self):
        self.__first__ = None
        self.__last__ = None
        self.__numbers__ = 0
    
    def is_empty(self):
        return self.__first__ == None

    def size(self):
        return self.__numbers__

    def enqueue(self, item):
        self.__numbers__ += 1
        __temp__ = self.__last__
        self.__last__ = self.Node()
        self.__last__.item = item
        if self.is_empty():
            self.__first__ = self.__last__
        else:
            __temp__.nxt = self.__last__
    
    def dequeue(self):
        if self.is_empty():
            return
        
        self.__numbers__ -= 1
        __ret__ = self.__first__.item
        self.__first__ = self.__first__.nxt
        return __ret__

    def __iter__(self):
        return iter(self.dequeue, None)

    def __repr__(self):
        __temp__ = self.__first__
        __representation__ = str(__temp__.item)
        while(__temp__.nxt):
            if __temp__.nxt.item:
                __representation__ += '-->'
                __representation__ += str(__temp__.nxt.item)
            __temp__ = __temp__.nxt
        return __representation__





