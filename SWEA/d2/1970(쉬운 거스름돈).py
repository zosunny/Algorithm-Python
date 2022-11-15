T = int(input())

for t in range(T):
    N = int(input())
    n1 = N // 50000
    c1 = N % 50000
    n2 = c1 // 10000
    c2 = c1 % 10000
    n3 = c2 // 5000
    c3 = c2 % 5000
    n4 = c3 // 1000
    c4 = c3 % 1000
    n5 = c4 // 500
    c5 = c4 % 500
    n6 = c5 // 100
    c6 = c5 % 100
    n7 = c6 // 50
    c7 = c6 % 50
    n8 = c7 // 10

    print("#", t+1, sep="")
    print(n1, n2, n3, n4, n5, n6, n7, n8)