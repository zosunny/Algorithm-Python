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

# 자기보다 크고 무거운 사람이 몇 명인지 카운트해 자기 등수를 매기면 된다.
