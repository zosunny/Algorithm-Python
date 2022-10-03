import sys
input = sys.stdin.readline

n = int(input())
dot = list(map(int, input().split()))
dot2 = sorted(list(set(dot)))
dic = {dot2[i] : i for i in range(len(dot2))}
for j in dot:
    print(dic[j], end=" ")