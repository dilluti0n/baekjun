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

def dpr(arr,i,j):

	global r, c
	cnt = 0
	
	while arr[i][j] != '0' :
		cnt += 1
		i += 1
		j += 1
		
		if i >= r or j >= c or arr[i][j] == '0':
			return cnt - 1
		
	return cnt
	
def dpl(arr,i,j):

	global r, c
	cnt = 0
	
	while arr[i][j] != '0' :
		cnt += 1
		i += 1
		j -= 1
		
		if i >= r or j < 0 or arr[i][j] == '0':
			return cnt - 1
		
	return cnt

result = 0
temp = [[0 for col in range(c)] for row in range(r)]

for i in range(0,r):
	for j in range(0,c):
			temp[i][j] = [dpr(arr,i,j),dpl(arr,i,j)]
			
def check(i,j):
	global temp
	res = 0
	
	for k in range(1,min(temp[i][j][0],temp[i][j][1])+1):
		
		if i+k >= r or j+k >= c or j-k < 0:
			return res
		
		elif temp[i+k][j+k][1] >= k and temp[i+k][j-k][0] >= k :
			res = k
			
	return res

for i in range(0,r-2):
	for j in range(1,c-1):
		result = max(check(i,j),result)

print(result+1)

end = time.time()

print(f"{end - start:.5f} sec")