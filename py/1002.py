from sys import stdin
import math

t = int(stdin.readline())

for _ in range(t):
	x, y, r1, z, w, r2 = map(int, stdin.readline().split())
	d = math.sqrt((x-z)**2+(y-w)**2)
	
	if d == 0 and r1 == r2 and r1 != 0:
		print(-1)
		
	elif d == 0 and r1 == r2 :
		print(1)
	
	elif d == 0:
		print(0)
		
	elif abs(r1-r2) == d or r1 + r2 == d:
		print(1)
		
	elif abs(r1-r2) < d < r1 + r2 :
		print(2)
		
	else:
		print(0)