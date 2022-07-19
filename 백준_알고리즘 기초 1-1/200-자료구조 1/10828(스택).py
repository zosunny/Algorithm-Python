import sys
input = sys.stdin.readline

def push(x):
    stack.append(x)
def pop():
    if len(stack) == 0:         # 스택에 아무것도 없으면
        return -1
    else:
        return stack.pop()      # pop() 이용. 빼고 출력
def size():
    return len(stack)           # 들어있는 개수
def empty():
    if len(stack) == 0:         # 스택에 아무것도 없으면
        return 1
    else:
        return 0
def top():
    if len(stack) == 0:         # 스택에 아무것도 없으면
        return -1
    else:
        return stack[-1]        # 빼지 않고 출력

n = int(input())
stack = []
for _ in range(n):
    input_list = list(input().rstrip().split())
    order = input_list[0]           # 명령부분만
    if order == "push":             # 문자열 ""과 비교해야함
        push(input_list[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())