#include <assert.h>
#include <string.h>

char* getPermutation(int n, int k);

int main(void) {
    char *result1 = getPermutation(3, 3);
    assert(strcmp(result1, "213") == 0);

    char *result2 = getPermutation(4, 9);
    assert(strcmp(result2, "2314") == 0);

    char *result3 = getPermutation(3, 1);
    assert(strcmp(result3, "123") == 0);

    char *result4 = getPermutation(1, 1);
    assert(strcmp(result4, "1") == 0);

    char *result5 = getPermutation(9, 362880);
    assert(strcmp(result5, "987654321") == 0);

    return 0;
}