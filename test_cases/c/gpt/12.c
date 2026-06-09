#include <assert.h>
#include <stdbool.h>

bool isScramble(char* s1, char* s2);

int main(void) {
    assert(isScramble("great", "rgeat") == true);
    assert(isScramble("abcde", "caebd") == false);
    assert(isScramble("a", "a") == true);
    assert(isScramble("abc", "bca") == true);
    assert(isScramble("abcdefghijklmnopqrstuvwxyzabcd", "abcdefghijklmnopqrstuvwxyzabcd") == true);

    return 0;
}