#include <assert.h>
#include <string.h>

char* minWindow(char* s, char* t);

int main(void) {
    assert(strcmp(minWindow("ADOBECODEBANC", "ABC"), "BANC") == 0);

    assert(strcmp(minWindow("a", "a"), "a") == 0);

    assert(strcmp(minWindow("a", "aa"), "") == 0);

    assert(strcmp(minWindow("AAABBC", "AABC"), "AABBC") == 0);

    assert(strcmp(minWindow("aAaBbBcC", "ABC"), "AaBbBc") == 0);

    return 0;
}