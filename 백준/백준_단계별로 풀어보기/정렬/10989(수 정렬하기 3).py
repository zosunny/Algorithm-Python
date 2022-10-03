# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))   # 메모리 재할당 -> 효율적 사용 X
#
# nums.sort()
# for i in nums:
#     print(i)

import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * 10001      # 0 ~ 10000
for _ in range(n):
    nums[int(input())] += 1     # 입력받은 값을 인덱스로 가지는 자리에 +1
                                # 1을 3번 입력받으면 numa[1] = 3 이 됨
for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)