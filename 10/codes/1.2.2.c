// code by Vishweshwar
#include <stdio.h>

/* unit step: u(n) = 1 for n >= 0, 0 for n < 0 */
static int u(int n)
{
    return n >= 0 ? 1 : 0;
}

/* A.P. as a sequence: x(n) = (a + (n - 1)d) u(n - 1) */
static double x(double a, double d, int n)
{
    return (a + (n - 1) * d) * u(n - 1);
}

int main(void)
{
    const double d = -4.0, a7 = 4.0;

    /* x(7) = a + 6d = a7  ->  a = a7 - 6d */
    double a = a7 - 6.0 * d;
    printf("first term a = %.0f\n", a);

    for (int n = -1; n <= 9; n++)
        printf("n = %2d   x(n) = %6.1f\n", n, x(a, d, n));

    /* verify the given seventh term */
    return x(a, d, 7) == a7 ? 0 : 1;
}
