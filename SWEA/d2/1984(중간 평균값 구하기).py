T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))
    nums.sort()
    sum = 0
    for i in nums[1:9]:
        sum += i
    ans = round(sum / (len(nums)-2))
    print("#", t + 1, " ", ans, sep="")