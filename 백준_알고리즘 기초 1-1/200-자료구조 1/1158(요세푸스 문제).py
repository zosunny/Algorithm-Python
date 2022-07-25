import sys
input = sys.stdin.readline

n, k = map(int, input().split())
plist = list(i for i in range(1, n+1))

ans = []
num = 0

for _ in range(n):
    num += k-1
    if num >= len(plist):
        num %= len(plist)
    ans.append(str(plist.pop(num)))

print("<",", ".join(ans), ">", sep="")