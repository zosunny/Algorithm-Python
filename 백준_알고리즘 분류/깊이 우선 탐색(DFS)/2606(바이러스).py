import sys
input = sys.stdin.readline

def dfs(graph, v, visit):
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            dfs(graph, i, visit)
    return True

n = int(input())    # 컴퓨터의 수
p = int(input())    # 연결 컴퓨터 쌍

# 인접 노드 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(p):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [0] * (n+1)     # 방문 체크

dfs(graph, 1, visit)
print(sum(visit) - 1)