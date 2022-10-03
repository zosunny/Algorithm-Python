import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in str(n):
    nums.append(int(i))

nums.sort(reverse=True)

for j in nums:
    print(j, end="")