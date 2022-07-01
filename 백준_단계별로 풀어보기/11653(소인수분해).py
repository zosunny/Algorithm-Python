n = int(input())
num = 2

# 1.
# while num <= n:
#     try:
#         if n % num == 0:
#             print(num)
#             n = n // num
#         else:
#             num += 1
#     except:
#         break

#2.
while num <= n:
    if n == 1:
        break
    if n % num == 0:
        print(num)
        n = n // num
    else:
        num += 1