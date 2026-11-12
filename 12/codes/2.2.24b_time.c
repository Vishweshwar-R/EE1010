// code by Vishweshwar
// Times Gaussian elimination for random n x n systems and writes "n  seconds" to a file.
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static void gauss(int n, double *a)          /* a is n x (n+1), row-major */
{
    int w = n + 1;
    for (int k = 0; k < n - 1; k++)
        for (int i = k + 1; i < n; i++) {
            double m = a[i * w + k] / a[k * w + k];
            for (int j = k; j < w; j++) a[i * w + j] -= m * a[k * w + j];
        }
    double *x = malloc(n * sizeof(double));
    for (int i = n - 1; i >= 0; i--) {
        double s = a[i * w + n];
        for (int j = i + 1; j < n; j++) s -= a[i * w + j] * x[j];
        x[i] = s / a[i * w + i];
    }
    free(x);
}

int main(void)
{
    FILE *fp = fopen("codes/2.2.24b_time.dat", "w");
    if (!fp) { fprintf(stderr, "run this program from the 12/ folder\n"); return 1; }
    srand(1);
    for (int n = 100; n <= 1000; n += 100) {
        int w = n + 1;
        double *a = malloc((size_t)n * w * sizeof(double));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < w; j++) a[i * w + j] = (double)rand() / RAND_MAX;
            a[i * w + i] += n;                /* diagonally dominant: no zero pivots */
        }
        clock_t t0 = clock();
        gauss(n, a);
        double t = (double)(clock() - t0) / CLOCKS_PER_SEC;
        printf("n = %4d   time = %.4f s\n", n, t);
        fprintf(fp, "%d %.6f\n", n, t);
        free(a);
    }
    fclose(fp);
    return 0;
}
