# import sys
# input = sys.stdin.readline
#
# alpha_set = set(range(ord('a'),ord('z')+1))
#
# s = list(map(str,input()))
#
# for i in alpha_set:
#     if chr(i) in s:
#         print(s.index(chr(i)), end=' ')
#     else:
#         print(-1, end=' ')

def solution():
    S = input()
    for i in range(97,123):
        print(S.find(chr(i)), end=' ')

solution()