// code by Vishweshwar
#include <math.h>
#include <stdio.h>

static double fa(double x)  { return x * x + 48.0 * x - 324.0; }   /* (a) boat  */
static double dfa(double x) { return 2.0 * x + 48.0; }
static double fb(double x)  { return x * x - 39.0 * x - 126.0; }   /* (b) train */
static double dfb(double x) { return 2.0 * x - 39.0; }

static double newton(double (*f)(double), double (*df)(double), double x0)
{
    double x = x0;
    for (int n = 0; n < 50 && fabs(f(x)) > 1e-12; n++) x = x - f(x) / df(x);
    return x;
}

int main(void)
{
    double a1 = newton(fa, dfa, 20.0), a2 = newton(fa, dfa, -100.0);
    double b1 = newton(fb, dfb, 60.0), b2 = newton(fb, dfb, -10.0);
    printf("(a) roots: %.9f and %.9f\n", a1, a2);
    printf("(b) roots: %.9f and %.9f\n", b1, b2);
    return (fabs(a1 - 6) < 1e-9 && fabs(a2 + 54) < 1e-9 && fabs(b1 - 42) < 1e-9 && fabs(b2 + 3) < 1e-9) ? 0 : 1;
}
