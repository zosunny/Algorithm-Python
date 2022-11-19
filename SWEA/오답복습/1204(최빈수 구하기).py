T = int(input())

for _ in range(T):
    t = int(input())
    arr = map(int, input().split())     #####
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    maxN = max(dict.values())           #####
    for k, v in dict.items():           #####
        if v == maxN:                   #####
            ans = k
            break
    print(f'#{t+1} {k}')