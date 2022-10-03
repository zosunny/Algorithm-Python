import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    data = input().rstrip()
    if data.count("(") == data.count(")"):
        print("YES")
    else:
        print("NO")