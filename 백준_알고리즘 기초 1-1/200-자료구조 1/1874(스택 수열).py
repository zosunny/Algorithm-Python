# 테스트케이스부터 틀림

import sys
input = sys.stdin.readline

def push(x):
    stack.append(x)
    print("+")
    print(stack)
def pop():
    stack.pop()
    print("-")
    print(stack)

n = int(input())
seq = []
stack = []
flag = 0
for _ in range(n):
    seq.append(int(input()))

for i in range(1,n+2):
    if seq[flag] in stack:
        pop()
        flag += 1
    else:
        push(i)
        i += 1