# 00시 00분 00초 ~ N시 59분 59초 사이
# 3이 들어가는 경우의 수는?

h = int(input())
cnt = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):     # 시, 분, 초 문자열로
                cnt += 1

print(cnt)