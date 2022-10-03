n = int(input())
result = list(range(2, n))
result.sort(reverse=True)
print(result)

for i in result:
    if n % i == 0:
        print(n // i)
        n = i

# for i in result:
#     if n % i == 0:
#         print(i)        //이렇게하면 나누는 수가 무조건 2->3->4 처럼 증가하게 됨..무조건 역으로
#         n = n // i