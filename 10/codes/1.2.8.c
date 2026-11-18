// code by Vishweshwar
#include <math.h>
#include <stdio.h>

/* f(x) = x^2 + 100x - 300000 and its derivative */
static double f(double x)  { return x * x + 100.0 * x - 300000.0; }
static double df(double x) { return 2.0 * x + 100.0; }

/* Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n) */
static double newton(double x0, int iters)
{
    double x = x0;
    printf("x0 = %.1f\n n          x_n            f(x_n)\n", x0);
    for (int n = 0; n <= iters; n++) {
        printf("%2d  %14.6f  %16.6f\n", n, x, f(x));
        x = x - f(x) / df(x);
    }
    return x;
}

int main(void)
{
    double r1 = newton(1000.0, 6);     /* converges to the positive root */
    double r2 = newton(-1000.0, 6);    /* converges to the negative root */
    printf("roots: %.6f and %.6f\n", r1, r2);

    /* verify with the factorisation (x - 500)(x + 600) */
    return (fabs(r1 - 500.0) < 1e-6 && fabs(r2 + 600.0) < 1e-6) ? 0 : 1;
}
