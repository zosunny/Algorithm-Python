arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:        # 원소가 1개면 종료
        return
    # 정렬하고자하는 데이터가 여러개면 퀵정렬 시작
    pivot = start           # 피벗 값 = 첫번째 원소
    left = start + 1
    right = end
    while(left <= right):   # 분할이 될때까지 (엇갈릴 때까지)
        # 피벗보다 큰 데이터 찾을 때까지 반복
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피벗보다 작은 데이터 찾을 때까지 반복
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        # left는 항상 오른쪽으로 가고 right은 항상 왼쪽으로 가기 때문에
        # 이 과정 자체를 '선형탐색'이라고 볼 수 있음
        if(left > right):       # min, max값의 자리가 엇갈리면 min과 pivot 자리를 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:                   # 아니라면 min값과 max값의 자리를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 후 왼쪽 부분과 오른쪽 부분 각각 퀵 정렬 수행(재귀적)
    quick_sort(arr, start, right-1)     # 왼쪽 부분
    quick_sort(arr, right+1, end)       # 오른쪽 부분

quick_sort(arr, 0, len(arr)-1)
print(arr)
