import sys

total_num = int(input())
xy_list = []

for i in range(total_num):
    xy = list(map(int, sys.stdin.readline().split()))
    xy_list.append(xy)
xy_list.sort()

for li in xy_list:
    result =" ".join(map(str, li))
    print(result)