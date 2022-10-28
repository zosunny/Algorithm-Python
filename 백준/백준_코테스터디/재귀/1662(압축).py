import sys
input = sys.stdin.readline

s = input().rstrip()
s = s[::-1]

stack = []
ans = ""

for i in range(len(s)):
    if s[i] == ")" or s[i-1] == "(":
        continue
    else:
        if s[i] == "(":
            stack.clear()
            stack.append(ans * int(s[i + 1]))
            ans = "".join(stack)
        else:
            ans = ans + s[i]

print(len(ans))