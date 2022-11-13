import sys
input = sys.stdin.readline

T = int(input())

def odd(i):
    ans = 0
    for x in tc:
        if x % 2 != 0:
            ans += x
    print("#", i+1, " ", ans, sep="")

for t in range(T):
    tc = list(map(int, input().split()))
    odd(t)