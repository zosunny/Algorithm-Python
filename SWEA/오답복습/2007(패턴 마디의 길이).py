T = int(input())

for t in range(T):
    arr = input()
    for i in range(1, 11):
        if arr[:i] == arr[i:2*i] and len(arr) % i < i:
            print(f'#{t+1} {i}')
            break