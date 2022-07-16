import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hear = set(input().rstrip() for _ in range(n))
see = set(input().rstrip() for _ in range(m))
both = list(hear & see)
both.sort()
print(len(both))
for i in both:
    print(i)