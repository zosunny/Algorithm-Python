import sys
input = sys.stdin.readline

def cal(s, i, num):             # 문자열, 탐색위치, 곱할 수
    leng = 0
    while i < len(s):
        if s[i] == "(":
            leng -= 1
            calcul, i = cal(s, i+1, int(s[i-1]))    # 재귀이용해  leng * num, i 값 반환
            leng += calcul          # 길이를 더하던 leng에 ex) 5(1 을 5*1로 계산한 결과 더함
        elif s[i] == ")":
            return leng * num, i    # 각각 calcul, i의 값으로
        else:
            leng += 1
        i += 1
    return leng * num, i        # cal(s, 0, 1)[0], cal(s, 0, 1)[1]

def solution(s):
    print(cal(s, 0, 1)[0])      # cal(s, 0, 1)[0] = leng * num

if __name__ == '__main__':
    solution(input().rstrip())