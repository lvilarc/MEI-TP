#include <assert.h>
#include <stdio.h>

int minCut(char* s);

int main(void) {
    assert(minCut("aab") == 1);
    assert(minCut("a") == 0);
    assert(minCut("ab") == 1);
    assert(minCut("aaaa") == 0);
    assert(minCut("abcde") == 4);
    return 0;
}