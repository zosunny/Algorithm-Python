T = int(input())

for t in range(T):
    sudo = [list(map(int, input().split())) for _ in range(9)]

    flag = 1
    for i in range(9):
        tmp = set()
        # 가로 탐색
        for j in range(9):
            tmp.add(sudo[i][j])
        if len(tmp) != 9:
            flag = 0
            tmp = set()
            break

    for i in range(9):
        tmp = set()
        # 세로 탐색
        for j in range(9):
            tmp.add(sudo[j][i])
        if len(tmp) != 9:
            flag = 0
            tmp = set()
            break
    # 사각형 탐색
    for i in range(9):
        for j in range(9):
            tmp = set()
            if i % 3 == 0 and j % 3 == 0:
                for x in range(3):
                    for y in range(3):
                        tmp.add(sudo[i+x][j+y])
                if len(tmp) != 9:
                    flag = 0
                    break
    # for x in range(0, 9, 3):
    #     for y in range(0, 9, 3):
    #         tmp = set()
    #         for z in range(3):
    #             for w in range(3):
    #                 tmp.add(sudo[x+z][y+w])
    #         if len(tmp) != 9:
    #             flag = 0
    #             break
    print("#", t+1, " ", flag, sep="")