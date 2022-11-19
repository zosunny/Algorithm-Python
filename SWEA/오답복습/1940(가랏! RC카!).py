T = int(input())

for t in range(T):
    N = int(input())
    speed = 0
    ans = 0
    for _ in range(N):
        lts = list(map(int, input().split()))
        if lts[0] == 1:
            speed += lts[1]     # speed는 계속 가속, 감속하며 값이 누적되고 있고
        if lts[0] == 2:
            speed -= lts[1]
            if speed < 0:
                speed = 0
        # 0일 땐 기존 speed값 더하면 됨
        ans += speed            # speed값 계속 누적 합이 답

    print(f'#{t+1} {ans}')