# n, k를 입력받아 n=1이 될 때까지 다음 조건을 수행
# 1. n-1
# 2. n/k (단, n이 k로 나누어 떨어져야 함)
# 이때 연산 횟수의 최솟값은?
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += n - target
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)