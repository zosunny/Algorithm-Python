import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

# 산술평균 : 총 합 / n
print(round(sum(nums) / n))

# 중앙값 : 오름차순의 중간 값
nums.sort()
print(nums[n//2])

# 최빈값
cnts = Counter(nums).most_common()
if len(cnts) > 1 and cnts[0][1] == cnts[1][1]:  # 최빈값이 같은 게 2개
    print(cnts[1][0])       # 두번째 최빈값 출력
else:
    print(cnts[0][0])       # 최빈값 출력

# 범위 : 최대 - 최소
print(max(nums) - min(nums))