# 문자열 S가 주어질 때 모든 알파벳은 오름차순 정렬
# 모든 숫자의 합은 그 뒤에 출력한다.
# ex. K1A5CB7 -> ABCK13

s = input()
ans = []
tmp = 0

for x in s:
    if x.isalpha():         # isalpha() : 알파벳이면 true 아니면 false
        ans.append(x)       # isdigit() : 숫자면 true 아니면 false
    else:
        tmp += int(x)

ans.sort()
if tmp != 0:
    ans.append(str(tmp))

print(''.join(ans))