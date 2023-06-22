from sys import stdin
import time
'''
r, c = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(r)]
'''

r,c = 175, 175
arr = []
for i in range(r):
    arr.append([])
    for j in range(c):
        arr[i].append('1')

start = time.time()


def dp(arr,i,j,ind):

	global r, c
	cnt = 0
	
	while arr[i][j] != '0' and i < r and j < c and i > 0 and j > 0:
		cnt += 1
		i += -1 ** ind[0]
		j += -1 ** ind[1]
		
	return cnt
		

'''
def check(arr,n,f):
    global r, c
    pseudo = []
    
    if arr[f[0]][f[1]] == '0':
        return False
    
    for i in range(n-1):
        f[0] += 1
        f[1] += 1
        pseudo.append(arr[f[0]][f[1]])
        
    if pseudo == [1] * (n-1):
    	return True
    	
        if arr[f[0]][f[1]] == '0':
            return False

    return True
'''

result = 0
indl = [[2,2],[2,1],[1,1],[1,2]]
temp = arr

for i in range(0,r):
	for j in range(0,c):
			temp[i][j] = [dp(arr,i,j,ind) for ind in indl]
			
def check(i,j):
	mm = []
	global m
	for ind in range(4):
		if temp[i][j][ind] == 0 or i < 0 or i >= c or j < 0 or j >= r:
			return False
			
		else :
			mm.append(temp[i][j][ind])
			i += temp[i][j][ind]*(-1 ** indl[ind])
			j += temp[i][j][ind]*(-1 ** indl[ind])
		
	if mm[0] == mm[1] and mm[1] == mm[2] and mm[2] == mm[3]:
		m = mm[0]
		return True
			
for i in range(0,r):
	for j in range(0,c):
		m = 0
		if check:
			result += m

print(result)
end = time.time()

print(f"{end - start:.5f} sec")