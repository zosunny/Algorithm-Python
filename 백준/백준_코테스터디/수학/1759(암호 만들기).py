import sys
input = sys.stdin.readline
from itertools import combinations

v = {'a', 'e', 'i', 'o', 'u'}

l, c = map(int, input().split())
alpha = list(input().split())        #c개의 문자가 있는 리스트

# co = list(alpha - v)      #자음:consonant
# vo = list(alpha & v)      #모음:vowel

ans = []
for i in combinations(alpha, l):                        #l개 뽑아 조합
    if len(set(i) & v) >= 1 and len(set(i) - v) >= 2:   #모음 1개이상 & 자음 2개이상 조건 만족시
        ans.append("".join(sorted(i)))                  #ans리스트에 담기(이때, 오름차순으로 조합)
    else:
        continue

for x in sorted(ans):   #오름차순으로
    print(x)            #출력