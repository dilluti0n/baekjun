from sys import stdin
from itertools import combinations
import math

t = int(stdin.readline())
for _ in range(t):
	n = int(stdin.readline())
	m = n // 2
	ps = []
	for _ in range(n):
		ps.append(list(map(int,stdin.readline().split())))
	
	vectorsum = [0,0]
	ls = []
	
	for i in range(n):
		vectorsum[0] += ps[i][0]
		vectorsum[1] += ps[i][1]
		
	for comb in list(combinations(ps,m)):
		if comb[0] == ps[1] : break # 중복계산방지
		p = [vectorsum[0],vectorsum[1]]
		for i in range(m):
			p[0] -= 2 * comb[i][0]
			p[1] -= 2 * comb[i][1]
		
		ls.append(math.sqrt(p[0] ** 2 + p[1] ** 2))
		
	print(min(ls))