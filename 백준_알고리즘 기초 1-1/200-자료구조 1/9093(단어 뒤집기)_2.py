import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = list(map(lambda x: x[::-1], input().split()))
    print(" ".join(s))      # 리스트를 " ".join 이용해
                            # 공백을 기준으로 조합해 출력