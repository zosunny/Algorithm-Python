def isPrime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True             # n == 2 or 3 일때 소수지만 range를 만족하지는 않음

m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)

print(int(4**0.5)+1)