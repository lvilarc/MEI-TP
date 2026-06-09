#include <assert.h>
#include <stdbool.h>
#include <stddef.h>

bool isScramble(char* s1, char* s2);

int main(void) {
    assert(isScramble("great", "rgeat") == true);
    assert(isScramble("abcde", "caebd") == false);
    assert(isScramble("a", "a") == true);
    assert(isScramble("abc", "abc") == true);
    assert(isScramble("abcdefghijklmnopq", "efghijklmnopqcadb") == false);
    return 0;
}