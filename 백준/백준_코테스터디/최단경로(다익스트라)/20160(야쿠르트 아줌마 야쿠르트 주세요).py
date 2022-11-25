import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize                               # int의 최댓값, int형 초과시 long으로 자동 변환
V, E = map(int, input().split())
nodes = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    nodes[u].append([v, w])
    nodes[v].append([u, w])
print(nodes)
sell_point = list(map(int, input().split()))    # 야쿠르트 아줌마가 야쿠르트 파는 10개 정점
me_start = int(input())                         # 내가 출발하는 정점 번호

def dijkstra(start):
    distances = [INF for _ in range(V+1)]
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost:
            continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

    return distances

answer = INF
total = 0
sell = sell_point[0]
my_distances = dijkstra(me_start)       # 내가 출발하는 지점으로부터의 최단거리 리스트 my_distances

for end in sell_point:
    distances = dijkstra(sell)
    distance = distances[end]           # 출발점에서 각 야구르트를 파는 곳까지 가는 최단 거리 distance

    if distance == INF:                 # 팔지 못한다면 continue
        continue
    total += distance                   # 거리 누적
    sell = end                          # 다음 출발지 sell = 이번에 도착한 end.
    my_distance = my_distances[end]     # 야쿠르트를 파는 end까지 가는 최단거리 my_distance

    if total >= my_distance:
        answer = min(answer, end)

if answer == INF:       # 야쿠르트 살 수 있는 정점이 없음
    print(-1)
else:
    print(answer)