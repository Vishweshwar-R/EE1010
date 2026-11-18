// code by Vishweshwar
#include <stdio.h>

int main(void)
{
    /* augmented matrix of x + y = 30, x - y = 14 */
    double a[2][3] = {{1, 1, 30}, {1, -1, 14}};

    /* R2 <- R2 - (a21/a11) R1 */
    double m = a[1][0] / a[0][0];
    for (int j = 0; j < 3; j++) a[1][j] -= m * a[0][j];
    printf("[ %4.1f %4.1f | %4.1f ]\n[ %4.1f %4.1f | %4.1f ]\n", a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]);

    /* back substitution */
    double y = a[1][2] / a[1][1];
    double x = (a[0][2] - a[0][1] * y) / a[0][0];
    printf("x = %.1f, y = %.1f\n", x, y);
    return (x == 22.0 && y == 8.0) ? 0 : 1;
}
