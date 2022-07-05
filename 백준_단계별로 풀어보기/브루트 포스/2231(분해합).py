n = int(input())

for i in range(1, n+1):
    nums = list(map(int, str(i)))       # 반복시 초기화 되어야 함
    cons = i + sum(nums)                # 생성자
    if cons == n:
        print(i)
        break

# 반례: 1, 1의 경우 생성자가 존재하지 않아
# 이 코드의 경우 출력값이 존재하지 않은 상태로 for문을 탈출하고 코드가 종료된다.
