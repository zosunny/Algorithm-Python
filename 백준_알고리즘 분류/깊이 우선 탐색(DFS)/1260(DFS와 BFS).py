import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visit):
    visit[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):     # 왜 이걸 해줘야만 정답이지..ㅠ?
    graph[i].sort()

visit = [False] * (N+1)
dfs(graph, V, visit)
print()
visit = [False] * (N+1)
bfs(graph, V, visit)