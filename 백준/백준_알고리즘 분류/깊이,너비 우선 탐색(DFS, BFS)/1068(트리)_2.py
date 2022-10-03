import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(d):
    t[d] = -2           # 제거 할 노드 -2 값으로 표시
    for i in range(n):
        if t[i] == d:   # 제거 할 노드를 부모로 갖는 노드들
            dfs(i)      # 재귀적으로 제거


n = int(input())
t = list(map(int, input().split()))
d = int(input())

dfs(d)

cnt = 0
for i in range(n):
    if t[i] != -2 and i not in t:   # t에 i가 있으면 i는 어떤 노드의 부모
        cnt += 1                    # 즉 i는 자식 노드가 있음을 의미함

print(cnt)