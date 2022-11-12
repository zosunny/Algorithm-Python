import sys
input = sys.stdin.readline

T = int(input())

for x in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    ans = 0
    maxP = price[-1]
    for i in price[::-1]:   # 뒤에서부터 돌면서
        if i > maxP:        # maxP에 최댓값을 넣으며
            maxP = i
        ans += maxP - i     # 최댓값보다 작으면 (현재값과)그 차이를 누적
    print("#", x+1, " ", ans, sep="")