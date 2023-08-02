#include <stdio.h>
#include <math.h>

int t;

void arrInput ( int* arr , int m ) {
	int *const arrEnd = arr + m;
	for (; arr < arrEnd; ++arr)
		scanf("%d", arr);
}

int main () {
	int x[4], c[3];
	
	int cnt, n;
	_Bool a, b;
	
	scanf("%d", &t);
	while (t--){
		arrInput (x, 4);
		cnt = 0;
		
		scanf("%d",&n);
		while (n--){
			arrInput (c, 3);
			a = (float) c[2] > sqrt( pow (x[0]-c[0], 2) + pow (x[1]-c[1],2));
			b = (float) c[2] > sqrt( pow (x[2]-c[0], 2) + pow (x[3]-c[1],2));
			
			if ( (!a && b)||(a && !b) )
				cnt++;
		}
		printf("%d\n", cnt);
	}
	return 0;
}