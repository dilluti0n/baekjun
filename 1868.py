from sys import stdin

n = int(stdin.readline())
graph = [[0,0] for _ in range(n-1)]
for i in range(n-1):
    graph[i][0] , graph[i][1] = map(int,stdin.readline().split())
    
dp = [[0,0] for _ in range(n)]
for i in range(n-1):