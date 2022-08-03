import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)        # 무한 재귀호출 방지

def dfs(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y+1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        dfs(x-1, y-1)
        return True
    return False
# 이문제는 어차피 섬의 수만 출력하면 되니까 행렬을 바꿔도 상관없으나
# 이렇게 하지는 말자..
while True:
    h, w = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 2차원 리스트의 맵 정보 입력
    graph = []
    for i in range(w):
        graph.append(list(map(int, input().split())))
    cnt = 0
    for i in range(w):
        for j in range(h):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)