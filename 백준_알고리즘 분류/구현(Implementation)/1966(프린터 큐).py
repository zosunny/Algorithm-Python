import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    que = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))
    cnt = 0
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx.popleft() == m:
                print(cnt)
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())
