import collections
import queue

#Double-en queue
collections.deque

q = queue.Queue()
lq = queue.LifoQueue()
l = []
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

# FIFO以外はLIFOと同じ動作
# for _ in range(3):
#     print(f'FIFO queue = {q.get()}')
#     print(f'LIFO queue = {lq.get()}')
#     print(f'list.pop =   {l.pop()}')
#     print(f'deque.pop =  {d.pop()}')

# FIFOのように制御する場合は、以下のようにする
#     # print(f'list.pop(0) =   {l.pop(0)}')
#     # print(f'deque.popleft =  {d.popleft()}')

#-----------------------------------------------------
# print(d)
# d.rotate()
# print(d)
# d.rotate()
# print(d)
# d.rotate()

# out --rotate
# deque([0, 1, 2])
# deque([2, 0, 1])
# deque([1, 2, 0])

# キュー制御-----------------------------------------------------
print(d)
d.extendleft('x') #左に挿入
d.extend('y')     #右に挿入
print(d)

# out --
# deque([0, 1, 2])
# deque(['x', 0, 1, 2, 'y']

# キューのクリア
d.clear()
print(d)
