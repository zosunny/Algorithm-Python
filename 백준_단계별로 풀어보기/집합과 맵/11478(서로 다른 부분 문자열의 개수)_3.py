import sys
input = sys.stdin.readline

s = input().rstrip()
part = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        part.add(s[i:j+1])
print(part)
print(len(part))