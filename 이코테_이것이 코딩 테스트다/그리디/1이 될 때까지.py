# n, k를 입력받아 n=1이 될 때까지 다음 조건을 수행
# 1. n-1
# 2. n/k (단, n이 k로 나누어 떨어져야 함)
# 이때 연산 횟수의 최솟값은?
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k         # k로 나누어 떨어지는 n에 가까운 수를 타겟으로 설정
    result += n - target        # 타겟이 될때까지 -1한 횟수 더함
    n = target                  # n = target 값으로 재설정
    if n < k:                   # n이 k값보다 작아지면
        break
    n //= k
    result += 1

result += (n-1)                 # k보다 작은 n이 1이 될때까지 -1 연산한 횟수 더해
print(result)