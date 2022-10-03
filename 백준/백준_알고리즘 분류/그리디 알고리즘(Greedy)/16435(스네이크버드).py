import sys
input = sys.stdin.readline

n, l = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in h:
    if i > l:
        break
    l += 1

print(l)