#include <stdlib.h>

double findMedianSortedArrays(int* a, int m, int* b, int n) {
    int total = m + n;
    int* merged = malloc(sizeof(int) * (total > 0 ? total : 1));
    int i = 0, j = 0, k = 0;
    while (i < m && j < n) merged[k++] = (a[i] <= b[j]) ? a[i++] : b[j++];
    while (i < m) merged[k++] = a[i++];
    while (j < n) merged[k++] = b[j++];
    double res;
    if (total % 2) res = merged[total / 2];
    else res = (merged[total / 2 - 1] + merged[total / 2]) / 2.0;
    free(merged);
    return res;
}
