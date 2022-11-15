T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    ltsN = list(map(int, input().split()))
    ltsM = list(map(int, input().split()))
    tmp = 0
    ans = []
    if N <= M:
        for i in range(M-N+1):
            for x in range(N):
                tmp += ltsM[i+x] * ltsN[x]
            ans.append(tmp)
            tmp = 0
    else:
        for i in range(N-M+1):
            for x in range(M):
                tmp += ltsN[i+x] * ltsM[x]
            ans.append(tmp)
            tmp = 0
    print(f'#{t+1} {max(ans)}')