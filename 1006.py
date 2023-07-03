from sys import stdin

t = int(stdin.readline())

for _ in range(t):
	n, w = map(int,stdin.readline().split())
	enmy = [0,0]
	for i in range(2):
		enmy[i] = list(map(int,stdin.readline().split()))
	
	ind = [[] for _ in range(n)]
	for i in range(n):
		ind[i].append(enmy[0][i] + enmy[0][i-1] <= w)
		ind[i].append(enmy[1][i] + enmy[1][i-1] <= w)
		ind[i].append(empy[0][i] + enmy[1][i] <= w)
		
		