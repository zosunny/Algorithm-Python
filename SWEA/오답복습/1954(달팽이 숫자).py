T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for t in range(T):
    N = int(input())
    visit = [[0]*N for _ in range(N)]
    r, c = 0, 0
    dist = 0
    for i in range(1, N*N+1):
        visit[r][c] = i
        r += dr[dist]
        c += dc[dist]
        if r < 0 or c < 0 or r >= N or c >= N or visit[r][c] != 0:
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist+1) % 4
            r += dr[dist]
            c += dc[dist]
    print(f'#{t+1}')
    for x in visit:
        print(*x)