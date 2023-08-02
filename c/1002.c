#include <stdio.h>
#include <math.h>

int t;

int main () {
	double x[7];
	double *arrPointer;
	double *const arrayEnd = x + 6;
	
	scanf ("%d", &t);
	while (t--) {
		arrPointer = x;
		for (; arrPointer < arrayEnd; ++arrPointer) 
			scanf ("%lf", arrPointer);
		*arrPointer = sqrt(pow((x[0]-x[3]),2)+pow((x[1]-x[4]),2));
		
		if ( !x[6] && x[2] == x[5] && x[2] )
			printf("-1");
			
		else if ( !x[6] && x[2] == x[5] )
			printf("1");
			
		else if ( !x[6] )
			printf("0");
			
		else if ( fabs(x[2] - x[5]) == x[6] || x[2] + x[5] == x[6] )
			printf("1");
			
		else if ( fabs(x[2] - x[5]) < x[6] && x[6] < x[2] + x[5])
			printf("2");
			
		else
			printf("0");
		
		printf("\n");
	}
		
	return 0;
}