import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

dic = {card2[i]: 0 for i in range(len(card2))}

for j in range(n):
    if card in dic.keys():      # card[j]를 빼먹음
        dic[card[j]] += 1수

for k in card2:
    print(dic[k], end=" ")