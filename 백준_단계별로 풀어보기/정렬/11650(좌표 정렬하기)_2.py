import sys
input = sys.stdin.readline

n = int(input())
xy_list = []

for _ in range(n):
    xy = list(map(int, input().split()))
    xy_list.append(xy)
xy_list.sort()

for li in xy_list:
    result =" ".join(map(str, li))
    print(result)