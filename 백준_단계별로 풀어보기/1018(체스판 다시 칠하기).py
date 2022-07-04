#1. NXM 행렬이 주어졌을 때 몇개의 8X8 체스판을 만들 수 있는지
#2. 한 체스판 검사시 i+8개의 행과 j+8개의 열을 검사한다.
#3. 행과 열의 합이 짝수일때의 모든 타일은 같은 색을 가져야하고
#   행과 열의 합이 홀수일때의 모든 타일은 짝수일때의 타일과는 다른 색이어야 한다.
#4. 짝수일때 시작타일의 색이 w일때와 b일때로 나누어 체크하고
#   홀수일때 시작타일과는 다른 색인지 체크한다.
#5. w로 시작했을 때와 b로 시작했을 때 고쳐야하는 타일수를 list에 담아 min값을 출력한다.

n, m = map(int, input().split())
board = []
repair = []
for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        first_w = 0             # 첫번째 칸을 흰색으로 시작할 때
        first_b = 0             # 첫번째 칸을 검은색으로 시작할 때
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:            # (짝 짝) (홀 홀) 행렬 처음과 색 같아야 함
                    if board[k][l] != 'W':      # w로 시작했는데 w가 아니면
                        first_w = first_w + 1
                    if board[k][l] != 'B':      # b로 시작했는데 b가 아니면
                        first_b = first_b + 1
                else:                           # (짝 홀) (홀 짝) 행렬 색 처음과 색 달라야 함
                    if board[k][l] != 'B':      # w로 시작했는데 b가 아니면
                        first_w = first_w + 1
                    if board[k][l] != 'W':      # b로 시작했는데 w가 아니면
                        first_b = first_b + 1
        repair.append(first_w)
        repair.append(first_b)

print(min(repair))