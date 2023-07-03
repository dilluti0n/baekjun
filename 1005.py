from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
	n, k = map(int, stdin.readline().split())
	D = list(map(int, stdin.readline().split()))
	gu = [[] for _ in range(n)]
	indegree = [0] * n
	
	for _ in range(k):
		u, v = map(int,stdin.readline().split())
		gu[u-1].append(v) # u를 지으면 지을수있는 건물들
		indegree[v-1] += 1
		
	w = int(stdin.readline())
	
	result = [0] * n
	q = deque()
	for i in range(n):
		if indegree[i] == 0:
			q.append(i+1)
			
	while q:
		now = q.popleft()
		
		for node in gu[now-1]:
			indegree[node-1] -= 1
			if indegree[node-1] == 0:
				q.append(node)
				
			result[node-1] = max(result[node-1],result[now-1] + D[now-1])
			
		if now == w:
			break
			
	print(result[w-1]+D[w-1])