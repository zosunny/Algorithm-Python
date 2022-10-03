import sys
input = sys.stdin.readline

n, k = map(int, input().split())
plist = list(i for i in range(1, n+1))

ans = []
num = 0

for _ in range(n):
    num += k-1                          # 인덱스 0부터 시작이니까 -1해서 누적
    if num >= len(plist):               # 한 바퀴 넘어가면
        num %= len(plist)               # 찾는 인덱스 재정의
    ans.append(str(plist.pop(num)))     # plist에서 인덱스가 num인 값 pop

print("<",", ".join(ans), ">", sep="")