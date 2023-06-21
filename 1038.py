n = int(input())
if n > 1022 :
	result = -1
	
else : 
	if n in range(0,10) :
		res = [n]
		
	else :
		n = n - 10
		res = [0,1]

		while n != 0:
			ind = True
			for i in range(0,len(res)-1):
				if res[i]+1 < res[i+1]:
					res[i] = res[i]+1
					for j in range(0,i):
						res[j] = 0
					ind = False
					break
				
			if ind and res[len(res)-1]+1 < 10:
				res[len(res)-1] += 1
				for i in range(0,len(res)-1):
					res[i] = 0
			
			if ind and res[len(res)-1]+1 >= 10 :
				res.append(1)
				for i in range(0,len(res)-1):
					res[i] = 0
		
			n -= 1
		
	result = int(''.join(map(str, list(reversed(res)))))
		
print(result)
			

	


	
		