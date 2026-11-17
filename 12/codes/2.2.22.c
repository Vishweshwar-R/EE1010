// code by Vishweshwar
#include <math.h>
#include <stdio.h>

/* (a) the curves x^2 + y^2 = 16 and y^2 = 6x meet where f(x) = x^2 + 6x - 16 = 0   (a = 1) */
static double f(double x)  { return x * x + 6 * x - 16; }
static double df(double x) { return 2 * x + 6; }

/* trapezoidal rule for the integral of h over [a, b] with n intervals */
static double trap(double (*h)(double), double a, double b, int n)
{
    double w = (b - a) / n, s = 0.5 * (h(a) + h(b));
    for (int i = 1; i < n; i++) s += h(a + i * w);
    return w * s;
}
static double ha(double y) { return sqrt(16 - y * y) - y * y / 6; }          /* right minus left boundary */

/* (b) upper minus lower boundary of the triangle with vertices (-1,1), (0,5), (3,2) */
static double hb1(double x) { return (4 * x + 5) - (x + 5) / 4; }            /* -1 <= x <= 0 */
static double hb2(double x) { return (5 - x) - (x + 5) / 4; }                /*  0 <= x <= 3 */

int main(void)
{
    double x = 5.0;
    for (int n = 0; n < 50 && fabs(f(x)) > 1e-13; n++) x = x - f(x) / df(x);
    double y1 = sqrt(6 * x);
    printf("Newton-Raphson: x = %.9f, y = %.9f\n", x, y1);

    double Aa = 2 * trap(ha, 0, y1, 100000);
    printf("(a) area (a = 1) = %.6f, exact (4/3)(4 pi + sqrt 3) = %.6f\n", Aa, 4.0 / 3 * (4 * 3.14159265358979323846 + sqrt(3.0)));
    double Ab = trap(hb1, -1, 0, 1) + trap(hb2, 0, 3, 1);
    printf("(b) area = %.6f\n", Ab);
    return (fabs(x - 2) < 1e-9 && fabs(Aa - 19.0645619) < 1e-4 && fabs(Ab - 7.5) < 1e-12) ? 0 : 1;
}
