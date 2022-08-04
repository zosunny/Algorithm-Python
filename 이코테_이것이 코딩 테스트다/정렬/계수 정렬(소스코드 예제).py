arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(arr) + 1)  # 모든 범위 포함하는 리스트 선언

# O(N)
for i in range(len(arr)):   # 각 데이터에 해당하는 인덱스 값 증가
    cnt[arr[i]] += 1

# O(N+K)
for i in range(len(cnt)):   # 리스트에 기록된 정렬 정보 확인
    for j in range(cnt[i]):
        print(i, end=' ')   # 띄어쓰기 구분으로 카운트된 횟수만큼 인덱스 출력