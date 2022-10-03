import sys
input = sys.stdin.readline

def dic_input():            #걸그룹 사전 만들기~
    mem_stack = []
    group = input().rstrip()
    num = int(input())
    for _ in range(num):
        member = input().rstrip()
        mem_stack.append(member)
    group_dict[group] = mem_stack


n, m = map(int, input().split())
group_dict = {}

for _ in range(n):      #딕셔너리로 걸그룹 사전 생성
    dic_input()

for _ in range(m):      #퀴즈 맞추기
    name = input().rstrip()
    x = int(input())
    if x == 0:
        for i in sorted(group_dict.get(name)):
            print(i)
    if x == 1:
        for key, value in group_dict.items():
            if name in value:
                print(key)