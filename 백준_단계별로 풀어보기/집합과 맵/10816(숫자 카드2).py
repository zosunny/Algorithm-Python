import sys
input = sys.stdin.readline

n = int(input())
sg = list(map(str, input().split()))
sg2 = set(sg)
cnt = 0
dic = {}
for i in sg2:
    cnt = sg.count(i)
    dic[i] = cnt

m = int(input())
nums = list(map(str, input().split()))
print(nums)

for j in nums:
    if j in sg2:
        print(dic[j], end=" ")
    else:
        print(0, end=" ")