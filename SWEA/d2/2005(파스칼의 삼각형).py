import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    ans = []
    for i in range(N):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(tmp)
    print("#", t+1, sep="")
    for x in ans:
        print(*x)