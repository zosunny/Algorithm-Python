import sys
from collections import Counter
input = sys.stdin.readline

n = input().rstrip()
card = list(map(int, input().split()))
m = input().rstrip()
test = list(map(int, input().split()))

cnt = Counter(card)     # Counter({10:3, 3:2, -10:2, 7:1, 6:1, 2:1})

for i in test:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")