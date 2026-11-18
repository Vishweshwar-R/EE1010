// code by Vishweshwar
#include <math.h>
#include <stdio.h>

/* p(x) = 2x^4 - 9x^3 + 5x^2 + 3x - 1 and p'(x) */
static double p(double x)  { return (((2 * x - 9) * x + 5) * x + 3) * x - 1; }
static double dp(double x) { return ((8 * x - 27) * x + 10) * x + 3; }

static double newton(double x0)
{
    double x = x0;
    for (int n = 0; n < 50 && fabs(p(x)) > 1e-13; n++) x = x - p(x) / dp(x);
    return x;
}

int main(void)
{
    const double start[4] = {5.0, 0.0, 1.2, -1.0};
    const double exact[4] = {2 + 1.7320508075688772, 2 - 1.7320508075688772, 1.0, -0.5};
    int ok = 1;
    for (int i = 0; i < 4; i++) {
        double r = newton(start[i]);
        printf("x0 = %5.1f  ->  root = %.9f\n", start[i], r);
        if (fabs(r - exact[i]) > 1e-9) ok = 0;
    }
    return ok ? 0 : 1;
}
