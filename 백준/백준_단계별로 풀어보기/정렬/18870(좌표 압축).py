import sys
input = sys.stdin.readline

n = int(input())
mark = [0] * n
dots = list(map(int, input().split()))
origin = dots[:]                        # [ 2 4 -10 4 -9 ]
dots.sort()                             # [ -10 -9 2 4 4 ]
# print("origin: ", origin)
# print("dots: ", dots)
for i in range(1, n):
    if dots[i] != dots[i-1]:
        mark[i] += mark[i-1] + 1
    else:
        mark[i] = mark[i-1]
# print("mark: ", mark)

for k in origin:
    for l in range(n):
        if k == dots[l]:
            print(mark[l], end=" ")
            break