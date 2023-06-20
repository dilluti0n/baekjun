from sys import stdin
import math
N, M = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(N)]

def sqtest(n):
  return math.isqrt(n) ** 2 == n

def filter(a,i,j,d1,d2):
  result = 0
  while i in range(0,N) and j in range(0,M) :
    result *= 10
    result += int(a[i][j])
    if d1 == 0 and d2 == 0 :
    	break
    i += d1
    j += d2
  result = int(result)
  return result

res = -1
for i in range(N):
  for j in range(M):
    for d1 in range(-N,N):
      for d2 in range(-M,M):
        num = filter(arr,i,j,d1,d2)
        if sqtest(num):
          res = max(res,num)

print(res)