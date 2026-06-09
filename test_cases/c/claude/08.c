#include <stdio.h>
#include <string.h>
#include <assert.h>

char* getPermutation(int n, int k);

int main(void) {
    assert(strcmp(getPermutation(3, 3), "213") == 0);
    assert(strcmp(getPermutation(4, 9), "2314") == 0);
    assert(strcmp(getPermutation(3, 1), "123") == 0);
    assert(strcmp(getPermutation(1, 1), "1") == 0);
    assert(strcmp(getPermutation(9, 362880), "987654321") == 0);
    return 0;
}