#include <stdio.h>
#include <math.h>

int switch_var(int);

int main()
{
    int t;
    scanf("%d", &t);

    while (t-- > 0) {
        int x, y;

        scanf("%d %d", &x, &y);
        x = switch_var(y - x);
        printf("%d\n", x);
    }
    return 0;
}

int switch_var(int x)
{
    int n = (int) sqrt((double) x);

    if (n * n == x)
        return 2 * n - 1;
    if (x <= n * (n + 1))
        return 2 * n;
    else
        return 2 * n + 1;
}
