t = int(input())
for i in range(t):
    R, S = input().split()
    result = ''
    for j in S:
        result += j * int(R)
    print(result)