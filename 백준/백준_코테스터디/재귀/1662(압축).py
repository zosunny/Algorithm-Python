import sys
input = sys.stdin.readline

def cal(s, i, num):             # 문자열, 탐색위치, 곱할 수
    leng = 0
    while i < len(s):
        if s[i] == "(":
            leng -= 1
            calcul, i = cal(s, i+1, int(s[i-1]))
            leng += calcul
        elif s[i] == ")":
            return leng * num, i    # 각각 calcul, i의 값으로
        else:
            leng += 1
        i += 1
    return leng * num, i

def solution(s):
    print(cal(s, 0, 1)[0])      # num만 반환

if __name__ == '__main__':
    solution(input().rstrip())