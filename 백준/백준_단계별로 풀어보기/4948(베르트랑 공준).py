def isPrime(num):
    if num == 1:
        return False
    for k in range(2, int(num**0.5)+1):
        if num % k == 0:
            return False
    return True

numbers = []

while True:
    n = int(input())
    if n == 0:
        for i in numbers:
            cnt = 0
            for j in range(i+1, (2*i)+1):
                if isPrime(j):
                    cnt += 1
            print(cnt)
        break
    else:
        numbers.append(n)