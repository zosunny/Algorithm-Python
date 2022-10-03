import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hear = set(input().rstrip() for _ in range(n))      # 듣도 못한 사람
see = set(input().rstrip() for _ in range(m))       # 보도 못한 사람
both = list(hear & see)     # 듣도 보도 못한 사람
both.sort()                 # 사전 순 정렬
print(len(both))            # 인원 수
for i in both:
    print(i)