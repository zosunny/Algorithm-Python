T = int(input())

def div(N, i, ans, cnt):
    if N % i == 0:
        cnt += 1
        div(N//i, i, ans, cnt)
    else:
        ans.append(cnt)

for t in range(T):
    N = int(input())
    ans = []
    cnt = 0
    div(N, 2, ans, cnt)
    div(N, 3, ans, cnt)
    div(N, 5, ans, cnt)
    div(N, 7, ans, cnt)
    div(N, 11, ans, cnt)
    print(f'#{t + 1} ', end="")
    print(*ans)