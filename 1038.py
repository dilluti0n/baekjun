def func(n):
	if n in range(0,10) :
		result = n

		
	else :
		n = n - 10
		res = [0,1]

		while n != 0:
			ind = True
			for i in range(0,len(res)-1):
				if res[i]+1 < res[i+1]:
					res[i] = res[i]+1
					for j in range(0,i):
						res[j] = j
					ind = False
					break
				
			if ind and res[len(res)-1]+1 < 10:
				res[len(res)-1] += 1
				for i in range(0,len(res)-1):
					res[i] = i
				ind = False
			
			if ind and res[len(res)-1]+1 >= 10 :
				res.append(len(res))
				for i in range(0,len(res)-1):
					res[i] = i
			n -= 1
			
			if res == [0,1,2,3,4,5,6,7,8,9,10]:
				return -1
					
		result = int(''.join(map(str, list(reversed(res)))))
	
	
	return result


n = int(input())
output = func(n)
print(output)