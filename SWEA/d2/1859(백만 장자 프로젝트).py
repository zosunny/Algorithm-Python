import sys
input = sys.stdin.readline

def solv(x):
    ans = 0
    buy = []
    while True:
        if len(price) == 0:
            print("#", x, " ", ans, sep="")
            break
        else:
            if price[0] < max(price):
                buy.append(price.pop(0))
            elif price[0] == max(price):
                ans += price.pop(0) * len(buy) - sum(buy)
                buy = []

T = int(input())

for x in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    solv(x+1)