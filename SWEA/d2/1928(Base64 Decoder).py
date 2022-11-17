# base64 라이브러리 사용
from base64 import b64decode

T = int(input())

for t in range(T):
    word = input()
    ans = b64decode(word).decode('UTF-8')
    print(f'#{t+1} {ans}')