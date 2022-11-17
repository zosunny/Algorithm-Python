T = int(input())

for x in range(T):
    P, Q, R, S, W = map(int, input().split())
    # A사
    a = W * P
    # B사
    if W <= R:
        b = Q
    else:
        b = Q + (W-R) * S
    print(f'#{x+1} {min(a, b)}')