import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

dist = []
for i in range(1, n):
    dist.append(sensor[i] - sensor[i-1])    # 센서들 거리의 차를 넣은 리스트

dist.sort(reverse=True)         # 거리의 차 내림차순 정렬
print(sum(dist[k-1:]))          # k-1 번째부터 출력