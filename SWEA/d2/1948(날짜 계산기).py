T = int(input())

days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]  # 누적 날짜 미리 저장

for t in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    ans = (days[m2-1] + d2) - (days[m1-1] + d1) + 1
    print(f'#{t+1} {ans}')