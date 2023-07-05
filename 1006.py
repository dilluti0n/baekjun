from sys import stdin
a = [0]*20000
b = [0]*20000
c = [0]*20000
w = 0
n = 0
e = [0,0]

def rec(init):
	global a,b,c,w,n,e
	for i in range(init,n):
		a[i+1] = min(b[i]+1,c[i]+1)
		
		if e[0][i] + e[1][i] <= w:
			a[i+1] = min(a[i+1],a[i]+1)
			
		if i > 0 and e[0][i-1]+e[0][i] <= w and e[1][i-1]+e[1][i] <= w:
			a[i+1] = min(a[i+1],a[i-1]+2)
		
		if i < n-1 :
			b[i+1] = a[i+1]+1
			c[i+1] = a[i+1]+1
			
			if e[1][i] + e[1][i+1] <= w:
				b[i+1] = min(b[i+1],c[i]+1)
		
			if e[0][i] + e[0][i+1] <= w:
				c[i+1] = min(c[i+1],b[i]+1)

t = int(stdin.readline())

for _ in range(t):
	n, w = map(int,stdin.readline().split())
	for i in range(2):
		e[i] = list(map(int,stdin.readline().split()))
		
	a[0] = 0
	b[0] = 1
	c[0] = 1
	
	rec(0)
	res = a[n]
	
	if n > 1 and e[0][0] + e[0][n-1] <= w:
		a[1] = 1
		b[1] = 2
		if e[1][0] + e[1][1] <= w: b[1] = 1
		c[1] = 2
		
		rec(1)
		res = min(res,b[n-1]+1)
	
	if n > 1 and e[1][0] + e[1][n-1] <= w:
		a[1] = 1
		b[1] = 2
		c[1] = 2
		if e[0][0] + e[0][1] <= w: c[1] = 1
		
		rec(1)
		res = min(res,c[n-1]+1)
		
	if n > 1 and e[1][0] + e[1][n-1] <= w and e[0][0] + e[0][n-1] <= w:
		a[1] = 0
		b[1] = 1
		c[1] = 1
		
		rec(1)
		res = min(res,a[n-1]+2)
		
	print(res)