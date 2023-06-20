import math
pseudo = list(map(int, input().split()))

N = pseudo[0]
M = pseudo[1]
arr = [[int(i) for i in str(pseudo[j])] for j in range(2,N+2)]

def sqtest(n):
  return math.isqrt(n) ** 2 == n

def filter(a,i,j,d1,d2):
  result = 0
  while i in range(0,N) and j in range(0,M) :
    result *= 10
    result += a[i][j]
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