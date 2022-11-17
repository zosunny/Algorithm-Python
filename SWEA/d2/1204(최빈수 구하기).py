T = int(input())

for _ in range(T):
    n = int(input())
    arr = map(int, input().split())
    dict = {}
    for i in arr:
        if i in dict:       # dict에 key값이 i인게 있으면
            dict[i] += 1
        else:
            dict[i] = 1
    maxV = max(dict.values())   # dict 중 max인 value값
    for k, v in dict.items():
        if v == maxV:
            ans = k             # 그때의 key값을 찾음
            break
    print(f'#{n} {k}')