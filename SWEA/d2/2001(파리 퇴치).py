import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arrN = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for m in range(M):
                for n in range(M):
                    sum += arrN[i+m][j+n]
            ans.append(sum)
    print("#", t+1, " ", max(ans), sep="")