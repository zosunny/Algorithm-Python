n = int(input())
nums = 666
cnt = 0

while True:
    if "666" in str(nums):
        cnt += 1
        if n == cnt:
            break
    nums += 1

print(nums)