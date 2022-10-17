import sys
input = sys.stdin.readline

# def overlap(nums, n):
#     nums.sort()
#     flag = 0
#     for i in range(n):                    #이중반복문->시간초과
#         temp = nums[i]
#         for j in nums[i+1:]:
#             if temp == j[:len(temp)]:
#                 flag = 1
#                 break
#     if flag == 0:
#         print('YES')
#     else:
#         print('No')
#
# def num_book():
#     n = int(input())
#     nums = []
#     for _ in range(n):
#         tmp = input().rstrip().replace(" ", "")
#         numb.append(tmp)
#     overlap(nums, n)
#
# t = int(input())
# for _ in range(t):
#     num_book()

# => 시간초과


def num_book():
    n = int(input())
    nums = []
    flag = 0
    for _ in range(n):
        tmp = input().rstrip().replace(" ", "")
        nums.append(tmp)
    nums.sort()
    for i in range(n-1):        #어차피 정렬하고 비교하니까 앞뒤 번호들만 비교하면 됨
        if nums[i] == nums[i+1][:len(nums[i])]:     #앞번호=뒷번호[앞번호길이만큼] 이면!
            flag = 1
    if flag == 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    num_book()