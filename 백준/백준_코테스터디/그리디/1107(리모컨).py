import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M == 0:
    print(len(str(N)))
else:
    broken = list(map(int, input().split()))

    if N == 100:
        print(0)
    else:
        ltsN = [int(x) for x in str(N)]
        newN = []
        for i in ltsN:
            while True:
                if i in broken:
                    if i == 1:
                        i -= 1
                    else:
                        i += 1
                else:
                    newN.append(i)
                    break
        print(newN)
        print(ltsN)
        ans = abs(int(''.join(map(str, newN))) - int(''.join(map(str, ltsN)))) + len(ltsN)

        print(ans)