#include <stdlib.h>

int candy(int* ratings, int n) {
    if (n == 0) return 0;
    int* c = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) c[i] = 1;
    for (int i = 1; i < n; i++)
        if (ratings[i] > ratings[i - 1]) c[i] = c[i - 1] + 1;
    for (int i = n - 2; i >= 0; i--)
        if (ratings[i] > ratings[i + 1] && c[i] <= c[i + 1]) c[i] = c[i + 1] + 1;
    int sum = 0;
    for (int i = 0; i < n; i++) sum += c[i];
    free(c);
    return sum;
}
