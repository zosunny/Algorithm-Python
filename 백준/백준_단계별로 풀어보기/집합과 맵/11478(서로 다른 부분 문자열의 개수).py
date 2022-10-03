import sys
input = sys.stdin.readline

s = input().rstrip()
part = set()
for i in range(len(s)):
    for j in range(1, len(s)):      # i로 고쳐야 함
        part.add(s[i:j])
# print(part)
print(len(part))