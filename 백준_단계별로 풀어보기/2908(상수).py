a, b = input().split()      # input은 다 문자열 취급
a = int(a[::-1])            # 슬라이싱 에서 step을 -1 하면 역순
b = int(b[::-1])
print(max(a,b))