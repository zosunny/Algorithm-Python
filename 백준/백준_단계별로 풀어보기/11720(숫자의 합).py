n = int(input())
num_list = list(map(str, input()))

result = 0

for i in num_list:
    result += int(i)

print(result)