T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxN = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for x in range(M):
                for y in range(M):
                    tmp += arr[i+x][j+y]
            if maxN < tmp:
                maxN = tmp
    print(f'#{t+1} {maxN}')