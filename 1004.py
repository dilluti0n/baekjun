from sys import stdin
from math import sqrt

t = int(stdin.readline())

for _ in range(t):
	x, y, z, w = map(int,stdin.readline().split())
	cnt = 0
	n = int(stdin.readline())
	for _ in range(n):
		cx, cy, r = map(int,stdin.readline().split())
		a = r > sqrt((x-cx)**2+(y-cy)**2)
		b = r > sqrt((z-cx)**2+(w-cy)**2)
		
		if (not a and b) or (a and not b):
			cnt += 1
			
	print(cnt)