import sys
input = sys.stdin.readline

n = int(input())
score = 0
result = 0

for i in range(n):
    input_list = list(input())
    for j in input_list:
        if j == 'O':
            score += 1
        else:
            score = 0
        result += score
    print(result)
    result = 0