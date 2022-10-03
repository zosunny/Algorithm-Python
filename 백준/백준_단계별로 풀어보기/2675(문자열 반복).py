def repeat(t):
    for i in range(t):
        R, S = map(str, input().split())
        repeat_str(R,S)

def repeat_str(R,S):
    for i in str(S):
        print(i * int(R), end='')
    print()

t = int(input())
repeat(t)