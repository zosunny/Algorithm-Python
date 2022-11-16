T = int(input())

for t in range(T):
    N = int(input())
    ans = []
    for _ in range(N):
        c, k = map(str, input().split())
        for _ in range(int(k)):
            ans.append(c)

    print(f'#{t+1}')
    for i in range(len(ans)):
        if i != 0 and i % 10 == 0:
            print()
        print(ans[i], end="")
    print()