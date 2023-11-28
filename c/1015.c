#include <stdio.h>

void quicksort(short [], short [], int, int);
void swap(short [], short [], int, int);
void printarray(short [], int);

int main()
{
    char N, i;
    scanf("%d", (int *) &N);
    short A[N], index[N], P[N];

    for (i = 0; i < N; i++) {
        scanf("%d", (int *) &A[i]);
        index[i] = i;
    }
    quicksort(A, index, 0, N-1);
    for (i = 0; i < N; i++)
        P[index[i]] = i;
    printarray(P, N);
    
    return 0;
}

void quicksort(short A[], short P[], int left, int right)
{
    int i, last;
    
    if (left >= right)
        return;
    
    swap(A, P, left, (left + right) / 2);
    
    last = left;
    for (i = left + 1; i <= right; i++)
        if (A[i] < A[left])
            swap(A, P, ++last, i);
    
    swap(A, P, left, last);
    quicksort(A, P, left, last - 1);
    quicksort(A, P, last + 1, right);
}

void swap(short A[], short P[], int i, int j)
{
    short temp;
    
    temp = A[j];
    A[j] = A[i];
    A[i] = temp;
    temp = P[j];
    P[j] = P[i];
    P[i] = temp;
}

void printarray(short arr[], int N)
{
    int i;

    for (i = 0; i < N - 1; i++)
        printf("%d ", arr[i]);
    printf("%d", arr[N-1]);
}