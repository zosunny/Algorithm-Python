import sys
input = sys.stdin.readline

mark = []
n = int(input())
dots = list(map(int, input().split()))
origin = dots[:]                        # [ 2 4 -10 4 -9 ]
dots.sort(reverse=True)                 # [ -10 -9 2 4 4 ]

# for i in range(len(dots)-1):
#     if dots[i] != dots[i+1]:
#         mark[]