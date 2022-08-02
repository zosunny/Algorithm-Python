import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(y, x):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(y, x-1)
        dfs(y, x+1)
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y-1, x-1)
        dfs(y-1, x+1)
        dfs(y+1, x-1)
        dfs(y+1, x+1)
        return True
    return False


while True:
    w, h = map(int,input().split())
    if w == 0 & h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)