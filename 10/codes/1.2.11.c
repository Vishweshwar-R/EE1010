// code by Vishweshwar
#include <math.h>
#include <stdio.h>

/* terms x0, x0+D, x0+2D, x0+3D with sum 32  ->  x0 = 8 - 1.5 D */
static double f(double D)
{
    double t1 = 8 - 1.5 * D, t2 = 8 - 0.5 * D, t3 = 8 + 0.5 * D, t4 = 8 + 1.5 * D;
    return 15 * t1 * t4 - 7 * t2 * t3;      /* = 0 for the ratio 7 : 15 */
}
static double df(double D) { return -64.0 * D; }

static double newton(double D0)
{
    double D = D0;
    for (int n = 0; n < 50 && fabs(f(D)) > 1e-12; n++) D = D - f(D) / df(D);
    return D;
}

int main(void)
{
    double D1 = newton(3.0), D2 = newton(-3.0);
    printf("D = %.9f or %.9f\n", D1, D2);
    double x0 = 8 - 1.5 * D1;
    printf("terms: %.1f %.1f %.1f %.1f\n", x0, x0 + D1, x0 + 2 * D1, x0 + 3 * D1);
    return (fabs(D1 - 4) < 1e-9 && fabs(D2 + 4) < 1e-9) ? 0 : 1;
}
