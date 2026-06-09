#include <assert.h>
#include <stdio.h>

int numDistinct(char* s, char* t);

int main(void) {
    assert(numDistinct("rabbbit", "rabbit") == 3);
    assert(numDistinct("babgbag", "bag") == 5);
    assert(numDistinct("a", "a") == 1);
    assert(numDistinct("abc", "abcd") == 0);
    assert(numDistinct("aaaa", "aa") == 6);

    printf("All tests passed.\n");
    return 0;
}