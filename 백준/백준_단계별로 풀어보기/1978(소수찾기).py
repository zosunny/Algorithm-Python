def solution(n, numbers):
    for i in numbers:
        for j in range(1, i):
            if i % j == 0 and j != 1:
                n -= 1
    if 1 in numbers:
        print(n-1)
    else:
        print(n)

n = int(input())
numbers = list(map(int, input().split()))

solution(n, numbers)