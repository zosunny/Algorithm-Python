import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

dic = {card2[i] : 0 for i in range(m)}

for j in range(n):
    if card[j] in dic.keys():
        dic[card[j]] += 1

for k in card2:
    print(dic[k], end=" ")