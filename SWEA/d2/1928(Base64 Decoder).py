# base64 라이브러리 사용
# from base64 import b64decode
#
# T = int(input())
#
# for t in range(T):
#     word = input()
#     ans = b64decode(word).decode('UTF-8')
#     print(f'#{t+1} {ans}')

T = int(input())

decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/']

for t in range(T):
    s = list(input())
    w = ''
    origin = ''
    for i in range(len(s)):
        idx = decode.index(s[i])        # 알파벳 -> 표1 숫자로 변환
        binN = str(bin(idx))[2:]        # 표1 숫자 -> 2진수로 변환 + 0b 제거
        while len(binN) < 6:            # 앞에 0추가해 6bit 2진수로!
            binN = '0' + binN
        w += binN                       # 6자리가 되면 w에 추가
    for x in range(0, len(w), 8):       # 8bit 씩 잘라보기
        e = int(w[x:x+8], 2)            # 8bit의 2진수 -> 10진수로 변환
        origin += chr(e)                # 10진수의 아스키코드 값 -> 문자로 변환
    print(f'#{t+1} {origin}')