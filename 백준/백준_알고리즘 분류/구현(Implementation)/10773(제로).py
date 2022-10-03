import sys
input = sys.stdin.readline

k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
        continue
    stack.append(n)
print(sum(stack))