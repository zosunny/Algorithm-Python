n = int(input())
numbers = list(map(int, input().split()))
cnt = 0

for i in numbers:
    check = 0
    if i == 1:              # 2~n 판단 전에 1일때 먼저 예외처리
        continue
    for j in range(2, i):
        if i % j == 0:      # 나누어 지는게 있으면
            check = 1       # 상태를 1로 만들고
    if check == 0:          # 반복문 후 상태가 0이면 (나누어지는 수가 없으면)
        cnt += 1            # 카운트 +1
print(cnt)