import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arrN = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N-M+1):          # N-M+1 범위까지의 idx까지만
        for j in range(N-M+1):
            sum = 0
            for m in range(M):      # 해당 idx에서 MXM 범위의 값
                for n in range(M):
                    sum += arrN[i+m][j+n]   # 누적(=파리채에 죽는 파리 수)
            ans.append(sum)
    print("#", t+1, " ", max(ans), sep="")