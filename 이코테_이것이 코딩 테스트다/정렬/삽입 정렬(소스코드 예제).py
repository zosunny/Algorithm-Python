arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):   # 인덱스 i부터 1까지 1씩 감소하며 반복
        if arr[j] < arr[j-1]:   # 현재 데이터가 왼쪽 데이터보다 작으면
            arr[j], arr[j-1] = arr[j-1], arr[j] # 자리를 바꿔 왼쪽으로 이동
        else:                   # 현재 데이터가 왼쪽 데이터보다 크면
            break               # 이동하지 않음

print(arr)