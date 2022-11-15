T = int(input())

for t in range(T):
    N = int(input())
    lts = list(map(int, input().split()))
    lts.sort()
    # print("#", t+1, " ", sep="", end="")
    # for x in lts:
    #     if x == lts[-1]:
    #         print(x)
    #         break
    #     print(x, end=" ")

    print(f'#{t + 1} ', end="")
    print(*lts)