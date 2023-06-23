from sys import stdin

r, c = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(r)]

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
	
	if arr[i][j] == '0' :
		return -1
		
	global temp
	res = 0
	
	for k in range(min(temp[i][j][0], temp[i][j][1]), 0, -1):
		
		if i+k >= r or j+k >= c or j-k < 0:
			break
		
		elif temp[i+k][j+k][1] >= k and temp[i+k][j-k][0] >= k :
			res = k
			break
			
	return res

for i in range(0,r):
	for j in range(0,c):
		result = max(check(i,j),result)

print(result+1)