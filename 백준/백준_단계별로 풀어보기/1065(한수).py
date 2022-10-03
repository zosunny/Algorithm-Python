def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        numbers = list(map(int,str(i)))     #i 각 자리를 분리하고 다시 int형으로
        if i < 100:
            cnt += 1                        #두자리 수는 무조건 등차수열을 이룸
        elif numbers[1]-numbers[0] == numbers[2]-numbers[1]:
            cnt += 1
    return cnt

n = int(input())
print(hansu(n))