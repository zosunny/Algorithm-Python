T = int(input())

for t in range(T):
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            ans -= i
        else:
            ans += i
    print("#", t+1, " ", ans, sep="")