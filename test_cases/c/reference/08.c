#include <stdlib.h>

char* getPermutation(int n, int k) {
    int fact[11];
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
    int avail[10];
    for (int i = 0; i < n; i++) avail[i] = i + 1;
    char* res = malloc(n + 1);
    k--;
    for (int i = 0; i < n; i++) {
        int f = fact[n - 1 - i];
        int idx = k / f;
        k %= f;
        res[i] = '0' + avail[idx];
        for (int j = idx; j < n - 1 - i; j++) avail[j] = avail[j + 1];
    }
    res[n] = '\0';
    return res;
}
