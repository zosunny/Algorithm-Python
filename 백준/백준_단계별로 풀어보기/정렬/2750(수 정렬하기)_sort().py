n = int(input())
# nums = [int(input()) for _ in range(n)]
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

for k in nums:
    print(k)