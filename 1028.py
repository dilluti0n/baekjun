from sys import stdin

<<<<<<< HEAD
r, c = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(r)]


def diamove(n):
	res = []
	for i in range(n-1):
		res.append((1,1))
		res.append((1,-1))
		res.append((-1,-1))
		res.append((-1,1))
	return res


def check(arr,n,f):

	if arr[f[0]][f[1]] == '0':
		return False
		
	for move in diamove(n):
		f[0] += move[0]
		f[1] += move[1]
		if f[0] < 0 or f[1] < 0 :
			return False
		
		elif arr[f[0]][f[1]] == '0':
			return False
	
	return True
'''	
for n in range(375):
	for i in range(r):
		for j in range(c):
			f = [i,j]
			if check(arr,n,f):
				result = n

print(result)
'''
print(arr)
=======
N, M = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(N)]
>>>>>>> acfe04e3e1de2e0765a8e672c078b8f7830858a5
