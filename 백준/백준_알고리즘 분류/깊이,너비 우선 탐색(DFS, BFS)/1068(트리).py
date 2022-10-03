import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(graph, v, visit):
    for i in graph[v]:
        if len(graph[v]) > 1:
            dfs(graph, i, visit)
        visit[v] = 1

n = int(input())
tmp = list(map(int, input().split()))
d = int(input())

# 인접 리스트 그래프 생성
graph = [[] for _ in range(n)]
for i in range(1, n):
    if d == 0:
        break
    if tmp[i] == d:
        break
    graph[tmp[i]].append(i)
    graph[i].append(tmp[i])

visit = [0] * n

dfs(graph, 0, visit)
print(sum(visit) - 1)