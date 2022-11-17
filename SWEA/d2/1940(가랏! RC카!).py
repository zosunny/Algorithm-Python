T = int(input())

for t in range(T):
    N = int(input())
    lts = [list(map(int, input().split())) for _ in range(N)]
    ans, tmp = 0, 0
    for i in lts:
        if i[0] == 1:
            tmp += i[1]
        elif i[0] == 2:
            tmp -= i[1]
            if ans < 0:     # 감속 속도가 더 클 경우 속도 = 0
                tmp = 0
        ans += tmp
    print(f'#{t+1} {ans}')