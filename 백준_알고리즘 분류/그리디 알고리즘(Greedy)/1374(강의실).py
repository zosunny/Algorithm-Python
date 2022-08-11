import sys
import heapq
input = sys.stdin.readline

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
l.sort(key = lambda x: x[1])
mh = []
cnt = 0
for x in l:
    while mh and mh[0] <= x[1]:
        heapq.heappop(mh)
    heapq.heappush(mh, x[2])
    cnt = max(cnt, len(mh))
print(cnt)