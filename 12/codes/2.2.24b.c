// code by Vishweshwar
#include <math.h>
#include <stdio.h>

#define N 3

static void print_aug(double a[N][N + 1], const char *title)
{
    printf("%s\n", title);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) printf("%8.3f ", a[i][j]);
        printf("| %8.3f\n", a[i][N]);
    }
}

int main(void)
{
    /* augmented matrix [A | b] of 2x+3y+10z=4, 4x-6y+5z=1, 6x+9y-20z=2 */
    double a[N][N + 1] = {{2, 3, 10, 4}, {4, -6, 5, 1}, {6, 9, -20, 2}};
    const double a0[N][N + 1] = {{2, 3, 10, 4}, {4, -6, 5, 1}, {6, 9, -20, 2}};
    print_aug(a, "[A|b]");

    /* forward elimination: R_i -> R_i - m R_k with m = a_ik / a_kk */
    for (int k = 0; k < N - 1; k++) {
        for (int i = k + 1; i < N; i++) {
            double m = a[i][k] / a[k][k];
            for (int j = k; j <= N; j++) a[i][j] -= m * a[k][j];
        }
        print_aug(a, "after elimination step");
    }

    /* back-substitution: x_i = (b_i - sum_{j>i} u_ij x_j) / u_ii */
    double x[N];
    for (int i = N - 1; i >= 0; i--) {
        double s = a[i][N];
        for (int j = i + 1; j < N; j++) s -= a[i][j] * x[j];
        x[i] = s / a[i][i];
    }
    printf("x = %.6f, y = %.6f, z = %.6f\n", x[0], x[1], x[2]);

    /* verify: residual of the original system */
    double r = 0.0;
    for (int i = 0; i < N; i++) {
        double s = -a0[i][N];
        for (int j = 0; j < N; j++) s += a0[i][j] * x[j];
        r += fabs(s);
    }
    printf("residual = %.2e\n", r);
    return (r < 1e-12 && fabs(x[0] - 0.5) < 1e-12 && fabs(x[1] - 1.0 / 3.0) < 1e-12
            && fabs(x[2] - 0.2) < 1e-12) ? 0 : 1;
}
