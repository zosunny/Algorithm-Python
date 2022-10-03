numbers_set = set(range(1, 10001))
generators_set = set()

for i in range(1, 10001):
    for j in str(i):            # i=850일때 j="8","5","0"
        i += int(j)             # 원래의 i값(850)에 8+5+0
    generators_set.add(i)       # 생성자가 존재하는 숫자들의 집합

self_number = sorted(numbers_set - generators_set)

for k in self_number:
    print(k)