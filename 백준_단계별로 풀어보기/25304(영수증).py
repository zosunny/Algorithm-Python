import sys
input = sys.stdin.readline

x = int(input())
N = int(input())
ans = 0
for _ in range(N):
    p, n = map(int, input().split())
    ans += p * n

if ans == x:
    print("Yes")
else:
    print("No")