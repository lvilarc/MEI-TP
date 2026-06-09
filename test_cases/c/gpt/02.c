#include <assert.h>
#include <stdbool.h>

bool isMatch(char* s, char* p);

int main(void) {
    assert(isMatch("aa", "a") == false);
    assert(isMatch("aa", "a*") == true);
    assert(isMatch("ab", ".*") == true);
    assert(isMatch("aab", "c*a*b") == true);
    assert(isMatch("aaaaaaaaaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*a*") == true);

    return 0;
}