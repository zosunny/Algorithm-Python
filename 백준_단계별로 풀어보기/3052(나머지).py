import sys

input = sys.stdin.readline
result = []

for i in range(10):
    n = int(input())
    result.append(n%42)

print(len(set(result)))