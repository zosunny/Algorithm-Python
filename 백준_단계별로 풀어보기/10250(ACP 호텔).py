def solution(H, W, N):
    rooms = list()
    for j in range(W):
        for k in range(H):
            rooms.append(str(k+1)+str('{0:02d}'.format(j+1)))
    print(rooms[N-1])

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    solution(H, W, N)