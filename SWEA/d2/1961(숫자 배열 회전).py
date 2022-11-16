T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도
    r1 = []
    for j in range(N):
        for i in range(N-1, -1, -1):
            r1.append(arr[i][j])
    # 180도
    r2 = []
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            r2.append(arr[i][j])
    # 270도
    r3 = []
    for j in range(N-1, -1, -1):
        for i in range(N):
            r3.append(arr[i][j])

    print(f'#{t + 1}')
    for x in range(0, N*N, N):          # N=3 일때 0, 3, 6에서 3개씩 출력하는 형태
        for y in range(N):
            print(r1[x+y], end="")
        print(end=" ")
        for y in range(N):
            print(r2[x+y], end="")
        print(end=" ")
        for y in range(N):
            print(r3[x+y], end="")
        print()