import sys
input = sys.stdin.readline

n = int(input())
nums = set(input().strip() for _ in range(n))
nums = list(nums)

nums.sort()
nums.sort(key=lambda i: len(i))
for i in nums:
    print(i)