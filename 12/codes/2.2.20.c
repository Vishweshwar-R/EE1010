// code by Vishweshwar
#include <math.h>
#include <stdio.h>

/* f(x) = sin 2x + cos 2x; f'(x) = 2 cos 2x - 2 sin 2x; f''(x) = -4 sin 2x - 4 cos 2x */
static double g(double x)  { return 2 * cos(2 * x) - 2 * sin(2 * x); }
static double dg(double x) { return -4 * sin(2 * x) - 4 * cos(2 * x); }

static double newton(double x0)
{
    double x = x0;
    for (int n = 0; n < 50 && fabs(g(x)) > 1e-13; n++) x = x - g(x) / dg(x);
    return x;
}

int main(void)
{
    const double pi = 3.14159265358979323846;
    double r1 = newton(0.5), r2 = newton(2.0);
    printf("zeros of f'(x): %.9f (pi/8 = %.9f), %.9f (5pi/8 = %.9f)\n", r1, pi / 8, r2, 5 * pi / 8);
    return (fabs(r1 - pi / 8) < 1e-9 && fabs(r2 - 5 * pi / 8) < 1e-9) ? 0 : 1;
}
