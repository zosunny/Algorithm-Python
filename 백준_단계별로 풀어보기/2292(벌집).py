n = int(input())
count = 1
cnt = 6
cnt_number = 6
ans = 1

while n > count:
    ans += 1
    count += cnt
    cnt += cnt_number

print(ans)