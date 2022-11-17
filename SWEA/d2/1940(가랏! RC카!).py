T = int(input())

for t in range(T):
    N = int(input())
    speed = 0
    dis = 0
    for i in range(N):
        lts = list(map(int, input().split()))
        if lts[0] == 1:
            speed += lts[1]
        elif lts[0] == 2:
            speed -= lts[1]
            if speed < 0:       # 현재 속도보다 감속 속도가 더 크면
                speed = 0       # 0 으로
        dis += speed

    print(f'#{t + 1} {dis}')


    # lts = [list(map(int, input().split())) for _ in range(N)]
    # ans, tmp = 0, 0
    # for i in lts:
    #     if i[0] == 1:
    #         tmp += i[1]
    #     elif i[0] == 2:
    #         tmp -= i[1]
    #         if ans < 0:     # 감속 속도가 더 클 경우 속도 = 0
    #             tmp = 0
    #     ans += tmp
    # print(f'#{t+1} {ans}')