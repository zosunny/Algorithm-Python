import sys
input = sys.stdin.readline

c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    avg_s = sum(scores[1:])/scores[0]
    cnt = 0
    for j in range(1, len(scores)):
        if scores[j] > avg_s:
            cnt += 1
    result = round(cnt / scores[0] * 100, 3)
    print(f"{result:.3f}%")