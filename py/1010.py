from sys import stdin

t = int(stdin.readline())
for _ in range(t):
	n, m = map(int,stdin.readline().split())
	
	a = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(m):
		a[0][i] = i+1
		
	for j in range(1,m):
		for i in range(1,min(j+1,n)):
			for k in range(i-1,j):
				a[i][j] += a[i-1][k]
				
	print(a[n-1][m-1])
