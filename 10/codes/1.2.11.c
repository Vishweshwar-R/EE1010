// code by Vishweshwar
#include <math.h>
#include <stdio.h>

/* top of the lighthouse A = (0, 100). The line of sight with depression angle t meets the
   ground at (x, 0). Unknowns (lambda, x):
       lambda sin t         = 100
       lambda cos t  -  x   = 0                        (Gauss elimination on a 2x3 matrix) */
static double ground_distance(double t)
{
    double a[2][3] = {{sin(t), 0.0, 100.0}, {cos(t), -1.0, 0.0}};
    double m = a[1][0] / a[0][0];
    for (int j = 0; j < 3; j++) a[1][j] -= m * a[0][j];     /* R2 <- R2 - m R1 */
    return a[1][2] / a[1][1];                               /* x */
}

int main(void)
{
    const double pi = 3.14159265358979323846;
    double x1 = ground_distance(pi / 4), x2 = ground_distance(pi / 6);
    printf("x1 = %.4f, x2 = %.4f, distance = %.4f m\n", x1, x2, x2 - x1);
    return (fabs(x1 - 100.0) < 1e-9 && fabs(x2 - x1 - 73.2051) < 1e-3) ? 0 : 1;
}
