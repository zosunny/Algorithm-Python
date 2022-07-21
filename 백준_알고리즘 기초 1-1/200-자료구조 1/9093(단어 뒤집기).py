import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = list(input().rstrip().split())
    r_word = []
    for i in s:
        r_word.append(i[::-1])  # 뒤집기
    ans = " ".join(r_word)
    print(ans)