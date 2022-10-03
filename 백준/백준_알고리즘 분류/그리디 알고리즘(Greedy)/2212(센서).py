import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(sensor[i] - sensor[i-1])    # 센서들 거리의 차를 넣은 리스트

dist.sort(reverse=True)     # 거리의 차 내림차순 정렬
for _ in range(k-1):        # 집중국이 K일때 k-1개의 거리차 제거
    dist.pop(0)             # 내림차순했을 때 가장 큰 (가장 먼)

print(sum(dist))            # 나머지 거리의 합이 곧 수신 가능 영역 거리의 합 최솟값