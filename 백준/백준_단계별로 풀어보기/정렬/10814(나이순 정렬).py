import sys
input = sys.stdin.readline

n = int(input())
members = []
for _ in range(n):
    a, b = map(str, input().split())
    members.append((int(a), b))
members.sort(key=lambda i: i[0])
for a, b in members:
    print(a, b)