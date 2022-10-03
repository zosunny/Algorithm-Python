import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    data = input().rstrip()
    while(True):
        if "()" in data:                    # 문자열에 () 가 있으면
            data = data.replace("()", "")   # 문자열에서 () 를 제거한다
        else:                               # 더이상 ()가 없으면
            break                           # 탈출
    if len(data) == 0:          # ()를 제거한 문자열에 아무것도 없으면
        print("YES")            # VPS 임
    else:
        print("NO")