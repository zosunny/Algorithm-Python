import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[a, b]])
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        for i in range(4):      # 상, 하, 좌, 우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:     # 범위내, 탐색X
                if graph[nx][ny] != 0:          # 빙산이면
                    visited[nx][ny] = True
                    q.append([nx, ny])          # 큐에 추가
                else:                           # 빙산 아니면
                    cnt[x][y] += 1              # 바닷물로 카운트
    return 1


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
year = 0

while True:                     # 모든 얼음이 녹을 때까지 무한반복
    ans = []
    visited = [[False] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    for i in range(N):          # 빙산 접촉 바닷물 확인
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                ans.append(bfs(i, j))
    for i in range(N):          # 빙산 깎기
        for j in range(M):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    if len(ans) == 0 or len(ans) >= 2:
        break
    year += 1

if len(ans) >= 2:
    print(year)
else:
    print(0)