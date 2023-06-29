from sys import stdin

n = int(stdin.readline())
graph = [[] for _ in range(n)]
dp = [0 for _ in range(n)]

for _ in range(n-1):
	u, v = map(int,stdin.readline().split())
	graph[u-1].append(v)
	dp[u-1] += 1
	
	graph[v-1].append(u)
	dp[v-1] += 1
	
cnt = 0
while dp != [0] * n :
	sstar = dp.index(max(dp))

	for node in graph[sstar]:
		graph[node-1].remove(sstar+1)
		dp[node-1] -= 1
	
	dp[sstar] = 0
	cnt += 1
	
print(cnt)