import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
tmp = ""
cnt = 0
ans = 0

for i in s:
    if i == ")":
        c, t = stack.pop()
        if cnt == 0:
            ans = ans * int(t) + c
        else:
            ans = cnt * int(t) + c
            cnt = 0

    elif i == "(":
        stack.append((cnt-1, tmp))
        cnt = 0
    else:
        tmp = i
        cnt += 1

if ans == 0:
    print(cnt)
else:
    print(ans)

