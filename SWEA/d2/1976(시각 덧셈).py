T = int(input())

for t in range(T):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    if h > 12:
        h -= 12
    m = m1 + m2
    if m >= 60:
        h += 1
        m -= 60
    print("#", t+1, " ", h, " ", m, sep="")