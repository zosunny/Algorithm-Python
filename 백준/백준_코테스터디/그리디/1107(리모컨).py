import sys
input = sys.stdin.readline

N = int(input())    # 이동할 채널
M = int(input())    # 고장난 버튼 수
broken = list(map(int, input().split()))    # 고장난 버튼

minN = abs(100 - N)     # 최소 이동

for i in range(1000000):    # 999999에서 이동 고려
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in broken:
            break
        if j == len(num)-1:     # 끝자리까지 탈없이 왔음
            minN = min(minN, abs(int(num)-N)+len(num))  # 최솟값 비교
print(minN)
