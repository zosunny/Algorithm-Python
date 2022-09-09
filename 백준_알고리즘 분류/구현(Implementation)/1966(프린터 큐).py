import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    que = deque(list(map(int, input().split())))    # 중요도
    idx = deque(list(range(n)))                     # 인덱스
    cnt = 0
    while que:
        if que[0] == max(que):      # 첫번째 요소가 최대값이면
            cnt += 1                # 카운트
            que.popleft()           # pop
            if idx.popleft() == m:  # 인덱스가 m과 같을 때
                print(cnt)          # 카운트 값 출력
        else:
            que.append(que.popleft())   # 왼쪽 값 pop해 append
            idx.append(idx.popleft())
