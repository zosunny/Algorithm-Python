import sys

input = sys.stdin.readline

result = []

n = int(input())

num_list = list(map(int, input().split()))

result.append(min(num_list))
result.append(max(num_list))

#print(' '.join(result))
print(" ".join(map(str, result)))   #.join을 하려면 str이어야 한다