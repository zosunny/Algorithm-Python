import sys
input = sys.stdin.readline

n = int(input())
nums = set(input().strip() for _ in range(n))       # sys로 문자열입력시 strip()안하면
nums = list(nums)                                   # 출력형식이 잘못되었습니다 뜸
nums.sort()
nums.sort(key=lambda i: len(i))     # sort(key = len) 랑 같음
for i in nums:
    print(i)