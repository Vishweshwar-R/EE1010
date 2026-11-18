// code by Vishweshwar
#include <math.h>
#include <stdio.h>

static double g(double x) { return fabs(x - 1) + fabs(x - 2) + fabs(x - 4); }

/* trapezoidal rule: T = h [ g(a)/2 + g(a+h) + ... + g(b-h) + g(b)/2 ] */
static double trapezoid(double a, double b, int n)
{
    double h = (b - a) / n, s = 0.5 * (g(a) + g(b));
    for (int i = 1; i < n; i++) s += g(a + i * h);
    return h * s;
}

int main(void)
{
    printf("N = 4     : %.6f\n", trapezoid(1, 5, 4));        /* nodes 1,2,3,4,5 contain the corners */
    printf("N = 1000  : %.6f\n", trapezoid(1, 5, 1000));
    return fabs(trapezoid(1, 5, 4) - 18.0) < 1e-12 ? 0 : 1;
}
