import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
dp = [0] * (n+1)
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

M = 0
for i in range(n):
    M = max(M, dp[i])   # 이전에 저장된 M의 값과 dp[i] 값 중 max값
    if i+t[i] > n:
        continue
    dp[i+t[i]] = max(M+p[i], dp[i+t[i]])    # 현재까지의 수익+오늘 상담 수익, 오늘 상담이 끝나는 시점의 수익 중 max값

print(max(dp))