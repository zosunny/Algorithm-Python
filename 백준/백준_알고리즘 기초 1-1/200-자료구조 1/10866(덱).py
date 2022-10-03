import sys
from collections import deque   # 덱 모듈 import
input = sys.stdin.readline

dq = deque()
n = int(input())

for _ in range(n):
    order_list = list(input().rstrip().split())
    order = order_list[0]
    if order == "push_front":
        dq.appendleft(order_list[1])    # 덱의 앞에 정수 추가
    elif order == "push_back":
        dq.append(order_list[1])
    elif order == "pop_front":
        if dq:                          # dq가 True면 (값이 있으면)
            print(dq.popleft())         # 덱의 앞의 수 pop
        else:
            print(-1)
    elif order == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(dq))
    elif order == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif order == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif order == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
