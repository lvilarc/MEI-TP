#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

bool isMatch(char* s, char* p);

int main(void) {
    assert(isMatch("aa", "a") == false);
    assert(isMatch("aa", "*") == true);
    assert(isMatch("cb", "?a") == false);
    assert(isMatch("", "") == true);
    assert(isMatch("adceb", "*a*b") == true);
    return 0;
}