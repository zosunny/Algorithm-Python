# 시간 복잡도가 O(nlog(n))인 정렬 알고리즘에는 병합 정렬/힙 정렬이 있다.
# 이때, 파이썬의 기본 정렬 함 또한 O(nlog(n))이다.
import sys
input = sys.stdin.readline

n = int(input())
# 예제의 최대값 n = 1,000,000 받으면 시간이 오래걸린다.
nums = [int(input()) for _ in range(n)]
nums.sort()
for i in nums:
    print(i)