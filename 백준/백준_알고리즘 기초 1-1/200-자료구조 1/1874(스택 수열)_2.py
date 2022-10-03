import sys
input = sys.stdin.readline

cnt = 1
flag = True
stack = []
op = []

n = int(input())
for i in range(n):
    num = int(input())
    while cnt <= num:       # num보다 같거나 작은 수 stack에 쌓음
        stack.append(cnt)
        op.append("+")
        cnt += 1
    if stack[-1] == num:    # num과 스택의 top 숫자가 같으면 제거
        stack.pop()         # ?!?!?
        op.append("-")
    else:
        flag = False        # 스택 수열을 만들 수 없음

if flag == False:
    print("NO")
else:
    for i in op:
        print(i)