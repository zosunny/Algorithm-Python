n = int(input())
sizes = []

for _ in range(n):
	w, h = map(int, input().split())
	sizes.append((w, h))

for i in sizes:								# 다음 사람 등수 계산할때
	rank = 1								# 등수 초기화
	for j in sizes:
		if i[0] < j[0] and i[1] < j[1]:		# 현재 나보다 크면
			rank += 1						# 등수 +1
	print(rank, end=" ")					# 내 등수 출력