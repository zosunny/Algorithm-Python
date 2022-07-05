n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# 삽입정렬 _ 최솟값 찾아 자리 바꿈
# for i in range(1, len(nums)):
#     while (i > 0) & (nums[i] < nums[i-1]):
#         nums[i], nums[i-1] = nums[i-1], nums[i]
#         i -= 1
for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]

for k in nums:
    print(k)