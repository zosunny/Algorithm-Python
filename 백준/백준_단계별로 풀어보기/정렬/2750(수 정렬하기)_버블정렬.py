n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# 버블정렬
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] > nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for k in nums:
    print(k)