import sys

stack_l = list(input()) # 커서 기준 왼쪽
stack_r = []            # 커서 기준 오른쪽
n = int(input())

for i in range(n):
    order_list = sys.stdin.readline().split()
    order = order_list[0]
    if order == "L" and stack_l:        # L이고 왼쪽에 값이 있으면(True면)
        stack_r.append(stack_l.pop())   # 왼쪽 값 pop해 오른쪽에 넣음
    elif order == "D" and stack_r:      # D이고 오른쪽에 값이 있으면(True면)
        stack_l.append(stack_r.pop())   # 오른쪽 값 pop해 왼쪽에 넣음
    elif order == "B" and stack_l:      # B이고 왼쪽에 값이 있으면(True면)
        stack_l.pop()                   # 왼쪽 값 삭제
    elif order == "P":                  # P면
        stack_l.append(order_list[1])   # 왼쪽에 입력 받은 값 추가

print("".join(stack_l + list(reversed(stack_r))))   # 오른쪽 리스트는 역순해서 붙여줘야 함