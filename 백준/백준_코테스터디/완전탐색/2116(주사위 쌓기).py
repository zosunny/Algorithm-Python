n = int(input())
dice = []
for _ in range(n):
    dice.append(list(map(int, input().split())))
pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

maxnum = 0                          # 최댓값
ans = []
for i in range(6):                  # 첫 번째 주사위 밑면 기준으로 반복
    max_side = []
    tmp = [1, 2, 3, 4, 5, 6]
    tmp.remove(dice[0][i])          # 첫 번째 주사위의 bottom 삭제
    next = dice[0][pair[i]]         # 첫 번째 주사위의 up 이자 다음 주사위의 bottom
    tmp.remove(next)                # 첫 번째 주사위의 up 삭제
    max_side.append(max(tmp))       # 옆면중 최댓값
    for j in range(1, n):           # 2~마지막 주사위까지 반복
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(next)
        next = dice[j][pair[dice[j].index(next)]]       # 아랫면 값의 인덱스로 윗면값 구함
        tmp.remove(next)                                # 윗면 삭제
        max_side.append(max(tmp))                       # 옆면중 최댓값
    max_side = sum(max_side)                            # 각 주사위별 옆면의 최대값 합
    ans.append(max_side)

print(max(ans))