import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    tc = input().rstrip()
    for i in range(1, 11):  # 마디 최대 길이 10
        if tc[:i] == tc[i:i*2] and len(tc.replace(tc[:i], '')) < i:     # 앞뒤가 반복되고, 남은글자가 마디길이보다 작아야함
            print("#", t+1, " ", i, sep="")
            break   # 안하면, #1 10 추가로 나옴