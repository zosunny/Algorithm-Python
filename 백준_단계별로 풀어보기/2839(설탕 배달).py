n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0:          # 5로 나누어 떨어지면
        cnt += n // 5       # 몫을 더함
        print(cnt)
        break
    n -= 3                  # 5로 나누어 떨어지지 않으면 3을 빼고
    cnt += 1                # + 1
else:                       # while의 조건에 맞지 않으면
    print(-1)               # (5로도 3으로도 안나눠 떨어지면) -1