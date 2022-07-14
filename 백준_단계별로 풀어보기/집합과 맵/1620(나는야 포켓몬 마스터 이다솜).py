import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mon = list(input().strip() for _ in range(n))
dic = {mon[i]: i+1 for i in range(len(mon))}
for _ in range(m):
    tmp = input().strip()
    if tmp.isalpha():
        print(dic[tmp])
    else:
        print(mon[int(tmp)-1])