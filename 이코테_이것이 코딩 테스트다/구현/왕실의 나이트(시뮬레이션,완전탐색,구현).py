# 8 X 8 좌표평면에서 나이트는 2가지 경우로 이동 가능하다 (정원 밖은 X)
# - 수평으로 두 칸 수직으로 한 칸
# - 수직으로 한 칸 수평으로 두 칸
# 이처럼 8 X 8 좌표평면상에서 나이트의 위치(ex. a1)가 주어졌을 때
# 나이트가 이동할 수 있는 경우의 수는?
# (단, 행 위치는 1-8로 열 위치는 a-h로 표현한다.)

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1   # 문자 -> 아스키코드: 컬럼의 위치 숫자로 변경 (1, 2, ...)
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0
for step in steps:
    next_row = row + step[0]    # 다음 행
    next_col = col + step[1]    # 다음 열
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:     # 범위 안이면
        cnt += 1                # 카운트

print(cnt)