T = int(input())

for t in range(T):
    word = input()
    flag = 0
    for i, j in zip(word, word[::-1]):
        if i != j:
            flag = 1
            break
    if flag == 1:
        print("#", t + 1, " ", 0, sep="")
    else:
        print("#", t + 1, " ", 1, sep="")
