#include <stdio.h>

void sort(short [], short [], int);
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
    sort(A, index, N);
    for (i = 0; i < N; i++)
        P[index[i]] = i;
    printarray(A, N);
    putchar('\n');
    printarray(P, N);
    
    return 0;
}

void sort(short a[], short index[], int N)
{
    for (int i = 0; i < N; i++)
        for (int j = i + 1; j < N; j++)
            if (a[i] > a[j])
                swap(a, index, i, j);
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