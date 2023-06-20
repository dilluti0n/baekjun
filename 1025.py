from sys import stdin
import math

N, M = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(N)]
res = -1

for i in range(N):
  for j in range(M):
    for d1 in range(-N,N):
      for d2 in range(-M,M):
      	num = ''
      	y, x = i, j
      	while y in range(0,N) and x in range(0,M) :
      		num += arr[y][x]
      		if d1 == 0 and d2 == 0 :
      			break
      		if math.isqrt(int(num)) ** 2 == int(num):
      			res = max(int(num),res)
      		y += d1
      		x += d2

print(res)