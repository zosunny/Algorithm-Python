import sys
import numpy
input = sys.stdin.readline

c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    avg_s = numpy.mean(scores[1:])
    cnt = 0
    for j in scores[1:]:
        if j > avg_s:
            cnt += 1
    result = round(cnt / scores[0] * 100, 3)
    print(f"{result:.3f}%")
