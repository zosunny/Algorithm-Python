n = int(input())
result = 0

for i in range(1, n+1):
    nums = list(map(int, str(i)))       # 반복시 초기화 되어야 함
    cons = i + sum(nums)                # 생성자
    if cons == n:
        result = i
        break
print(result)

# 1의 경우 생성자가 존재하지 않아 result의 초기값 0이 출력된다.