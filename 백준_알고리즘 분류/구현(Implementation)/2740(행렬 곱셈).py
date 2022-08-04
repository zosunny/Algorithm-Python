import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

ans = [[0]*k for _ in range(n)]     # 최종 행렬 : a의 행 X b의 열

# 행렬의 곱 연산 적용
for r in range(n):
    for c in range(k):
        tmp = 0
        for i in range(m):
            tmp += a[r][i] * b[i][c]
        ans[r][c] = tmp

for x in ans:
    print(*x)

