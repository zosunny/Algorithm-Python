import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
circle = deque([i for i in range(1, n+1)])
removed = []
while circle:
    circle.rotate(-(k-1))   # k-1만큼 왼쪽으로 리스트 이동
    removed.append(circle.popleft()) # k번째였던 수 제거

print(f'<{", ".join(map(str, removed))}>')  # f-string 문자열 포매팅 {}안의 값만 바뀌고 나머지는 일정