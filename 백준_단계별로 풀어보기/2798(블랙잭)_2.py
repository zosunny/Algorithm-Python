from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
maxValue = 0

for i, j, k in combinations(cards, 3):
    if maxValue < i+j+k <= m:
        maxValue = i+j+k

print(maxValue)