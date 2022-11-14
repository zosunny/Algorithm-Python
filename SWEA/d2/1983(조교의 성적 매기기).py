T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    stud = []
    for i in range(N):
        mid, fin, ass = map(int, input().split())
        tmp = [i+1, round((mid*0.35) + (fin*0.45) + (ass*0.2), 2)]
        stud.append(tmp)
    stud.sort(key=lambda x: -x[1])
    for x in range(len(stud)):
        if stud[x][0] == K:
            flag = x // (N*0.1)
    if flag == 0:
        ans = "A+"
    elif flag == 1:
        ans = "A0"
    elif flag == 2:
        ans = "A-"
    elif flag == 3:
        ans = "B+"
    elif flag == 4:
        ans = "B0"
    elif flag == 5:
        ans = "B-"
    elif flag == 6:
        ans = "C+"
    elif flag == 7:
        ans = "C0"
    elif flag == 8:
        ans = "C-"
    else:
        ans = "D0"
    print("#", t+1, " ", ans, sep="")