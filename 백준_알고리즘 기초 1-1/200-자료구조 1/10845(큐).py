import sys
input = sys.stdin.readline

def push(x):
    q.append(x)

def pop():
    if len(q) == 0:
        return -1
    else:
        return q.pop(0)

def size():
    return len(q)

def empty():
    if len(q) == 0:
        return 1
    else:
        return 0

def front():
    if len(q) == 0:
        return -1
    else:
        return q[0]

def back():
    if len(q) == 0:
        return -1
    else:
        return q[-1]

n = int(input())
q = []

for _ in range(n):
    order_list = list(input().rstrip().split())
    order = order_list[0]
    if order == "push":
        push(order_list[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())