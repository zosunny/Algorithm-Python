import sys
input = sys.stdin.readline

n = int(input())
card = set(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

for i in card2:
    if i in card:
        print(1, end=" ")
    else:
        print(0, end=" ")

# list에서 in 수행시 모든 요소를 처음부터 검사하면서 찾는 원소가 있는지 확인하지만,
# set은 해시로 구현되어 있어 x in set 이 x in list보다 일반적으로 더 빨리 동작하게 된다.