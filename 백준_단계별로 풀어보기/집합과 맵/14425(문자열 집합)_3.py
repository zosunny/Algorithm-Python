import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set(input() for _ in range(n))
cnt = 0
for _ in range(m):
    tmp = input()
    if tmp in s:
        cnt += 1

print(cnt)