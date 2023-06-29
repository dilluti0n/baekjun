from sys import stdin

t = int(stdin.readline())
f = [[1,0],[0,1]]
last = 1

for _ in range(t):
	n = int(stdin.readline())
	
	if n <= last : 
		print(f[n][0],f[n][1])
		
	else : 
		for i in range(last+1,n+1):
			f.append([f[i-1][0] + f[i-2][0],f[i-1][1] + f[i-2][1]])
		last = n
		print(f[n][0],f[n][1])