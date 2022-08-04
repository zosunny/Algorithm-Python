# 동빈이는 두 개의 배열 A와 B를 가지고 있다.
# 두 배열은 N개의 원소로 구성되어 있고 배열의 원소는 모두 자연수다.
# 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있다.
# 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라
# 두 원소를 서로 바꾸는 것을 말한다.
# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
# N, K 그리고 배열 A, B 정보가 주어졌을 때,
# 최대 K번의 바꿔치기 연산을 수행해 만들 수 있는
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성해보자.

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()                # a는 오름차순
b.sort(reverse=True)    # b는 오름차순

for i in range(k):                  # 최대 K번까지 교환가능
    if a[i] < b[i]:                 # a값보다 b값이 더 클때
        a[i], b[i] = b[i], a[i]     # 교환
    else:                           # a값이 더 커지는 순간
        break                       # 스탑

print(sum(a))