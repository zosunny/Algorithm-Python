import sys
input = sys.stdin.readline

def dic_input():            #걸그룹 사전 만들기~
    mem_stack = []
    group = input().rstrip()        #그룹 명
    num = int(input())              #멤버 수
    for _ in range(num):
        member = input().rstrip()   #멤버 이름
        mem_stack.append(member)    #리스트에 스택
    group_dict[group] = mem_stack   #{그룹명(group): [멤버이름으로 만든 리스트]}


n, m = map(int, input().split())
group_dict = {}     # {그룹명: 멤버이름~, 그룹명:멤버이름~}

for _ in range(n):
    dic_input()         #딕셔너리로 걸그룹 사전 생성

for _ in range(m):      #퀴즈 맞추기
    name = input().rstrip()
    x = int(input())
    if x == 0:
        for i in sorted(group_dict.get(name)):  #key(그룹명)값으로 value값 (사전순)출력
            print(i)
    if x == 1:
        for key, value in group_dict.items():   #key, value값 확인하며
            if name in value:                   #멤버이름이 value값에 있으면
                print(key)                      #그때의 key(그룹명)값 출력