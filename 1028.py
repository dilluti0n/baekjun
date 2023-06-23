from sys import stdin
import time

r, c = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(r)]
'''

r,c = 175, 175
arr = []
for i in range(r):
    arr.append([])
    for j in range(c):
        arr[i].append('1')
'''
start = time.time()

def dp(arr,i,j,ind):

	global r, c
	cnt = 0
	
	while arr[i][j] != '0' :
		cnt += 1
		i += (-1) ** ind[0]
		j += (-1) ** ind[1]
		
		if i >= r or j >= c or i < 0 or j < 0:
			return cnt -1
		
	return cnt

result = 0
indl = [[2,2],[2,1],[1,1],[1,2]]
temp = [[0 for col in range(c)] for row in range(r)]

for i in range(0,r):
	for j in range(0,c):
			temp[i][j] = [dp(arr,i,j,ind) for ind in indl]
			
def check(i,j):
	global temp
	res = 0
	
	for k in range(1,min(temp[i][j][0],temp[i][j][1])+1):
		
		y = i + 2 * k
		
		if y >= r :
			return res
		
		elif temp[y][j][2] >= k and temp[y][j][3] >= k :
			res = k
			
	return res

for i in range(0,r):
	for j in range(0,c):
		result = max(check(i,j),result)

print(result+1)

end = time.time()

print(f"{end - start:.5f} sec")