import sys
from collections import deque
input = sys.stdin.readline

# 깊이 우선 탐색은 for문만 돌면 연결된 인접 리스트들을 모두 탐색해 방문 처리가 가능함
def dfs(graph, v, visit):
    visit[v] = True                 # 현재 노드 방문 처리
    print(v, end=' ')               # 현재 방문 노드 출력
    for i in graph[v]:              # 현재 노드와 연결된 노드 탐색
        if not visit[i]:            # 연결된 노드의 방문 정보가 False면
            dfs(graph, i, visit)    # dfs 방문 (재귀적)

# 너비 우선 탐색은 큐에 맨 상층? 노드를 탐색하고 각각의 노드들 하나씩 pop하며
# 그 노드들에 연결된 다음 층 노드를 큐에 넣고 방문
# 또 그 노드들 하나씩 pop해 연결된 다음 층 노드를 큐에 넣고 방문
# 이러한 과정을 큐에 노드가 없을 때까지(모든 노드 방문) 계속 반복!
def bfs(graph, start, visit):
    queue = deque([start])      # 큐 구현 위해 deque 라이브러리 사용
    visit[start] = True         # 시작 노드부터 방문
    while queue:                # 큐에 값이 없을 때까지
        v = queue.popleft()     # 큐에서 맨 처음 들어간 원소 pop
        print(v, end=' ')       # pop한 원소는 방문 한 원소
        for i in graph[v]:      # 그 원소(노드)의 인접 노드 탐색
            if not visit[i]:    # 인접 노드의 방문 정보가 False면
                queue.append(i) # 큐에 넣고
                visit[i] = True # 방문 처리

N, M, V = map(int, input().split())

# 입력으로 연결 인접 리스트 그래프 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 연결 인접 리스트 정렬
# ex. [[4, 1], [5, 3], •••] -> [[1, 4], [3, 5], •••]
for i in range(1, N+1):     # 왜 이걸 해줘야만 정답이지..ㅠ?
    graph[i].sort()

visit = [False] * (N+1)
dfs(graph, V, visit)
print()
visit = [False] * (N+1)
bfs(graph, V, visit)