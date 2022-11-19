T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 90도
    arr1 = []
    for j in range(N):
        for i in range(N-1, -1, -1):
            arr1.append(arr[i][j])
    # 180도
    arr2 = []
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            arr2.append(arr[i][j])
    # 270도
    arr3 = []
    for j in range(N-1, -1, -1):
        for i in range(N):
            arr3.append(arr[i][j])

    print(f'#{t+1}')
    for x in range(0, N*N, N):
        for y in range(N):
            print(arr1[x+y], end="")
        print(end=" ")
        for y in range(N):
            print(arr2[x+y], end="")
        print(end=" ")
        for y in range(N):
            print(arr3[x+y], end="")
        print()