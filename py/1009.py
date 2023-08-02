from sys import stdin

t = int(stdin.readline())
for _ in range(t):
	a, b = map(int,stdin.readline().split())
	
	res = [1]
	for i in range(b):
		temp = res[i]*a
		if i > 0 and temp == res[1] : break
		res.append(temp)
		res[i+1] %= 10
	
	if res[len(res)-1] == 1:
		r = res[b % (len(res)-1)]
		
	elif res[len(res)-1] != 0:
		r = res[len(res)-1]
		
	else:
		r = 10
		
	print(r)