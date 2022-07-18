import sys
input = sys.stdin.readline

s = input().rstrip()
part = set()
for i in range(len(s)):
    for j in range(i+1, len(s)):
        part.add(s[i:j])
print(part)
print(len(part))