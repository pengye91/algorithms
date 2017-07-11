from queue import Queue
import sys

def josephus(q, n, m):
    ret_list = []
    for i in range(n):
        q.put(i)
    while not q.empty():
        for j in range(m):
            if j == (m - 1):
                ret_list.append(q.get())
            else:
                q.put(q.get())
    
    return ret_list

if __name__ == '__main__':
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    q = Queue(N)
    print(josephus(q, N, M))