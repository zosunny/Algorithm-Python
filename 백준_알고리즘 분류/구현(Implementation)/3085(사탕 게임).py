import sys
input = sys.stdin.readline

def check(b):
    n = len(b)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if b[i][j] == b[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
        cnt = 1
        for j in range(1, n):
            if b[j][i] == b[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
    return ans

n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp = check(board)
            if tmp > ans:
                ans = tmp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i + 1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = check(board)
            if tmp > ans:
                ans = tmp

            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)