import sys
input = sys.stdin.readline

A, B = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
ans = (a | b) - (a & b)
print(len(ans))