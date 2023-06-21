from sys import stdin

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

    global r, c
    if arr[f[0]][f[1]] == '0':
        return False
    
    for move in diamove(n):
        f[0] += move[0]
        f[1] += move[1]
        if f[0] < 0 or f[1] < 0 or f[0] > r-1 or f[1] > c-1:
            return False
        
        elif arr[f[0]][f[1]] == '0':
            return False
        
        else:
        	return True

result = 0

for n in range(min(r//2+2,c//2+2)):
	for i in range(r):
		for j in range(c):
			f = [i,j]
			if check(arr,n,f):
				result = n

print(result)