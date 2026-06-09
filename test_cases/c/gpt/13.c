#include <assert.h>

int numDistinct(char* s, char* t);

int main(void) {
    assert(numDistinct("rabbbit", "rabbit") == 3);

    assert(numDistinct("babgbag", "bag") == 5);

    assert(numDistinct("abc", "abcd") == 0);

    assert(numDistinct("abcdef", "abcdef") == 1);

    char s[1001];
    for (int i = 0; i < 1000; i++) {
        s[i] = 'a';
    }
    s[1000] = '\0';
    assert(numDistinct(s, "a") == 1000);

    return 0;
}