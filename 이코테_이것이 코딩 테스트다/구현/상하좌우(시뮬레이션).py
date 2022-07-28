# 공간의 크기가 N이고 이동계획이
#  L, R, U, D로 주어질 때 최종 도착 좌표는?
# (단, 시작 좌표 즉 왼쪽 맨 위는 (1, 1)이고
# 오른쪽 맨 아래는 (N, N)이며
# 공간을 넘어가는 이동의 경우 무시한다.)

n = int(input())            # 공간의 크기
x, y = 1, 1                 # 시작 좌표
plans = input().split()     # 이동 계획

dx = [0, 0, -1, 1]          # [L, R, U, D]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]              # 다음 x 좌표
            ny = y + dy[i]              # 다음 y 좌표
    if nx < 1 or nx > n or ny < 1 or ny > n:    # 공간 넘어가면
        continue                                # 무시
    x, y = nx, ny

print(nx, ny)