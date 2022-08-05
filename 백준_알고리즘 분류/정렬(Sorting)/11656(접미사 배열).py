import sys
input = sys.stdin.readline

s = input().rstrip()
ans = []
for i in range(len(s)):
    ans.append(s[i:])
ans.sort()
for x in ans:
    print(x)