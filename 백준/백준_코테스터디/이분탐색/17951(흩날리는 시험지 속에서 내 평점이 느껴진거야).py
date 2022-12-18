import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lts = list(map(int, input().split()))

ans = 0
start, end = 0, (10 ** 5 * 20) + 1      # 최대일 경우
while start <= end:
    mid = (start + end) // 2   # 그룹을 나누어야하는 최대점수
    group = 0
    score = 0
    for x in lts:
        score += x              # 점수의 누적 합이
        if score >= mid:        # 중간점수를 넘으면
            group += 1          # 그룹하나 생성..
            score = 0
    if group >= K:              # K개 이상이면 기준값이 작은 것
        ans = mid
        start = mid + 1
    else:                       # K개 이하면 기준값이 큰 것
        end = mid - 1
print(ans)