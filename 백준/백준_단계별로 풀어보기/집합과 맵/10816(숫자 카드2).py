import sys
input = sys.stdin.readline

n = int(input())
sg = list(map(str, input().split()))
sg2 = set(sg)          # 중복제거
cnt = 0
dic = {}
for i in sg2:
    cnt = sg.count(i)   # 상근이 카드 번호 마다 몇장이 있는지
    dic[i] = cnt        # 딕셔너리에 저장(추가)

m = int(input())
nums = list(map(str, input().split()))

for j in nums:                      # 입력받은 수가
    if j in sg2:                    # 상근이 카드에 있으면
        print(dic[j], end=" ")      # 딕셔너리에서 value값 출력
    else:
        print(0, end=" ")           # 없으면 0 출력