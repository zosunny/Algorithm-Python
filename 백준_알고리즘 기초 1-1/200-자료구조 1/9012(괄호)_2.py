import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    data = input().rstrip()
    while(True):
        if "()" in data:
            data = data.replace("()", "")
        else:
            break
    if len(data) == 0:
        print("YES")
    else:
        print("NO")