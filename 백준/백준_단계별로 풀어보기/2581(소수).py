m = int(input())
n = int(input())
result = []

for i in range(m, n+1):
    flag = 1
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = 0
    if flag == 1:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))