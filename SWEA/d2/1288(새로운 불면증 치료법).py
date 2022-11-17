T = int(input())

for t in range(T):
    N = int(input())
    cnt = 0
    num = set()
    while True:
        cnt += 1
        tmp = cnt * N
        for i in str(tmp):
            num.add(i)
        if len(num) == 10:
            break
    print(f'#{t+1} {cnt * N}')