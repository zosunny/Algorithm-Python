import sys
input = sys.stdin.readline

N = [i for i in range(1, int(input())+1)]
ans = []
cnt = 1
while N:
    if cnt % 2 == 0:
        N.append(N[0])
        N.pop(0)
    else:
        ans.append(N[0])
        N.pop(0)
    cnt += 1

print(' '.join(map(str, ans)))