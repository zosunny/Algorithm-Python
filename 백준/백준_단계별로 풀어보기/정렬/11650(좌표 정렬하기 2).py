import sys
input = sys.stdin.readline
nums = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    nums.append((x, y))

nums.sort(key=lambda i: (i[1], i[0]))

for i, j in nums:
    print(i, j)