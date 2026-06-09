#include <stdio.h>
#include <string.h>
#include <assert.h>

char* minWindow(char* s, char* t);

int main(void) {
    assert(strcmp(minWindow("ADOBECODEBANC", "ABC"), "BANC") == 0);
    assert(strcmp(minWindow("a", "a"), "a") == 0);
    assert(strcmp(minWindow("a", "aa"), "") == 0);
    assert(strcmp(minWindow("aa", "aa"), "aa") == 0);
    assert(strcmp(minWindow("aAbBcC", "ABC"), "ABcC") == 0);
    return 0;
}