from sys import stdin
import time
'''
r, c = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(r)]
'''

r,c = 100, 100
arr = []
for i in range(r):
    arr.append([])
    for j in range(c):
        arr[i].append('1')

start = time.time()
def diamove(n):
	res = []
	for i in range(n-1):
		res.append((1,1))
	for i in range(n-1):
		res.append((1,-1))
	for i in range(n-1):
		res.append((-1,-1))
	for i in range(n-1):
		res.append((-1,1))
	return res


def check(arr,n,f):
    global r, c
    if arr[f[0]][f[1]] == '0':
        return False
    
    for move in diamove(n):
        f[0] += move[0]
        f[1] += move[1]
        
        if arr[f[0]][f[1]] == '0':
            return False
    return True

result = 0

for n in range(1,min(r//2+2,c//2+2)):
	for i in range(0,r-2*n+2):
		for j in range(n-1,c-n+1):
			f = [i,j]
			if check(arr,n,f):
				result = n

print(result)
end = time.time()

print(f"{end - start:.5f} sec")