T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    puzz = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        cnt = 0
        # 가로 탐색
        for j in range(N):
            if puzz[i][j] == 1:
                cnt += 1
            if j == N-1 or puzz[i][j] == 0:     # 0으로 막히거나, 마지막칸이면
                if cnt == K:                    # 근데 그때 cnt == K 면! 하나 완성
                    ans += 1
                cnt = 0         # 다음 칸들도 확인해야하므로 초기화 필수

        # 세로 탐색
        for j in range(N):
            if puzz[j][i] == 1:
                cnt += 1
            if j == N - 1 or puzz[j][i] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0

    print("#", t+1, " ", ans, sep="")