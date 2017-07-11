class UnionFind():
    # __size 数组记录该节点包含的子孙节点的总数量，并不是总高度
    # 如果是扁平化的，则一样。
    __size = []
    __height = []
    __id = []
    __count = 0

    def __init__(self, N):
        self.__id = [i for i in range(N)]
        self.__size = [1 for i in range(N)]
        self.__height = [1 for i in range(N)]
        self.__count = N
    
    def find(self, i):
        _height = 1
        while(i != self.__id[i]):
            i = self.__id[i]
            # 指向爷爷节点，可以更扁平化
            self.__id[i] = self.__id[self.__id[self.__id[i]]]
            _height += 1
        if self.__height[i] < _height:  
            self.__height[i] = _height
        return i

    def union_find(self, p, q):
        if self.find(p) == self.find(q):
            return
        if self.__size(p) < self.__size(q): 
            self.__id[self.find(p)] = self.find(q)
            self.__size[q] += self.__size[p]
        else:
            self.__id[self.find(q)] = self.find(p)
            self.__size[p] += self.__size[q]
        
        # 使用高度来判断怎样union
        # if self.__height[p] < self.__height[q]:
            # self.__id[self.find(p)] = self.find(q)
            # self.__height[q] += 1
        # else:
            # self.__id[self.find(q)] = self.find(p)
            # self.__height[p] += 1
            
            
        self.__count -= 1
