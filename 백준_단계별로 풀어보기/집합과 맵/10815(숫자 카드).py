import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

for i in range(m):
    if card2[i] in card:
        print(1, end=" ")
    else:
        print(0, end=" ")