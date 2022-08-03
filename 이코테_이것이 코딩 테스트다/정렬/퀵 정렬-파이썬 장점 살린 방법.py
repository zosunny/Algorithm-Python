arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]      # 피벗 = 첫번째 원소
    tail = arr[1:]      # 피벗을 제외한 리스트
    # pivot과 pivot을 제외한 나머지 원소 리스트 비교하며 왼쪽 오른쪽 부분으로 분할
    left_side = [x for x in tail if x <= pivot]     # pivot 보다 작으면 왼쪽에
    right_side = [x for x in tail if x > pivot]     # pivot 보다 크면 오른쪽에
    # 분할 후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))