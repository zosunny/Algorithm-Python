# 모험가가 N명일 때 공포도가 X인 모험가는
# X명 이상의 그룹에 참가해야 한다.
# 모험가가 마을에 남아있어도 된다는 가정하에
# 여행을 떠날 수 있는 그룹 수의 최댓값은?

import sys
input = sys.stdin.readline

n = int(input())                            # 모험가의 수
data = list(map(int, input().split()))      # 공포도 입력받아 list로
data.sort()                                 # 공포도 오름차순 정렬

result = 0              # 총 그룹 수
cnt = 0                 # 현재 그룹의 모험가 수

for i in data:          # 공포도 순서대로 확인
    cnt += 1            # 모험가 수 +1
    if cnt >= i:        # 모험가 수 >= 공포도 가 되면
        result += 1     # 그룹 수 +1
        cnt = 0         # 그룹 결정되었으니 모험가 수 초기화

print(result)