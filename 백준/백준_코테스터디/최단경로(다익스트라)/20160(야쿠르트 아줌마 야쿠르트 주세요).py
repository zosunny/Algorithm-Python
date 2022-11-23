import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
node = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    node[u].append([v, w])
    node[v].append([u, w])
sell_spot = list(map(int, input().split()))
me = int(input())

