n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort()

for x, y in dots:
    print(x, y)