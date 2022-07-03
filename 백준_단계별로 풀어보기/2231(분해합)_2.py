n = int(input())
result = 0

for i in range(1, n+1):
    nums = list(map(int, str(i)))       # 반복시 초기화 되어야 함
    cons = i + sum(nums)                # 생성자
    if cons == n:
        result = i
        break
print(result)