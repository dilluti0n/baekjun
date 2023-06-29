from sys import stdin

t = int(stdin.readline())

for _ in range(t):
	n, k = map(int, stdin.readline().split())
	D = list(map(int, stdin.readline().split()))
	gd = [[] for _ in range(n)]
	
	for _ in range(k):
		u, v = map(int,stdin.readline().split())
		gd[v-1].append(u) # v를 짓기위해 지어야하는 건물들
		
	w = int(stdin.readline())
	
	memo = [-1 for _ in range(n)]
	init = []
	
	for i in range(n):
		if gd[i] == []:
			memo[i] = D[i]-1
			init.append(i)
			
	def dp(n):
		if memo[n-1] != -1:
			return memo[n-1]+1
				
				
		return memo[n-1] + 1
		
	print(dp(w))