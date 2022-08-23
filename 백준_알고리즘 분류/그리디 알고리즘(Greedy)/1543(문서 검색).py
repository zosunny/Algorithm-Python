import sys
input = sys.stdin.readline

s = input().rstrip()
w = input().rstrip()
newS = s.split(w)       # w를 구분자로 단어 쪼갬

print(len(newS)-1)