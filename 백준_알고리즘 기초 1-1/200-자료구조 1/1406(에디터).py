import sys
input = sys.stdin.readline

def shift_l():
    return 0
def shift_r():
    return 0
def del_l():
    return 0
def plus(x):
    return 0
n = list(input().rstrip())
N = len(n)
M = int(input())
for _ in range(M):
    order_list = list(input().rstrip().split())
    order = order_list[0]
    if order == "L":
        shift_l()
    elif order == "D":
        shift_r()
    elif order == "B":
        del_l()
    elif order == "P":
        plus(order_list[1])