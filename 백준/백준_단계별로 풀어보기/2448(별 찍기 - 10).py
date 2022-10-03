def draw(n):
    tmp =[]     # 별 담을 빈 리스트
    for i in range(3 * len(n)):     # 별의 줄 수가 3배씩 늘어남
        if i // len(n) == 1:        # 몫이 1일때 즉 행렬의 3,4,5 범위는 공백이 들어감
            tmp.append(n[i%len(n)] + " " * len(n) + n[i%len(n)])
        else:
            tmp.append(n[i%len(n)] * 3)
    return tmp

star = ["***", "* *", "***"]    # N=3일때
N = int(input())
cnt = 0

while N != 3:       # N이 3이 아닌 경우 반복
    N = N // 3
    cnt += 1        # cnt로 log 역할 ex. N=27, cnt

for _ in range(cnt):
    star = draw(star)   # 현재 별의 개수를 그 다음 함수의 인자로 넣음

for i in star:      # 리스트의 별 한줄씩 출력
    print(i)