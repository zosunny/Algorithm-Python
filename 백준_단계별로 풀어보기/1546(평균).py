import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
result = 0
maxN = max(numbers)

for i in range(n):
    numbers[i] = numbers[i]/maxN*100
    result += numbers[i]

print(result/n)