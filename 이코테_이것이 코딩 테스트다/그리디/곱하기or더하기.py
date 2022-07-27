# 문자열 S가 주어졌을 때 왼->오 순서대로
# +, x로 만들 수 있는 가장 큰 수 출력
import sys
input = sys.stdin.readline

data = input().rstrip()
result = int(data[0])

for i in range(1, len(data)):       # 인덱스 1부터 보기 시작
    num = int(data[i])              # num에 문자열의 각 자리의 수 대입
    if num <= 1 or result <= 1:     # num값이 1이하거나 result값이 1이하면
        result += num               # 더하고
    else:                           # 그 외에는
        result *= num               # 곱함

print(result)