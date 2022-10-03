def isPrime(n):
    cnt = 0
    for i in range(n+1, 2*n+1):
        if i == 1:
            continue
        for j in range(2, int(n**0.5)+1):
            if i % j == 0:
                break
        else:               # for-else: for문이 break로 끊기지 않고 끝까지 수행했을 때 수행하는 코드
            cnt += 1
    print(cnt)

while True:
    n = int(input())
    if n == 0:
        break
    isPrime(n)

