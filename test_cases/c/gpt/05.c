#include <assert.h>

int longestValidParentheses(char *s);

int main(void) {
    assert(longestValidParentheses("(()") == 2);
    assert(longestValidParentheses(")()())") == 4);
    assert(longestValidParentheses("") == 0);
    assert(longestValidParentheses("()(())") == 6);

    static char boundary[30001];
    for (int i = 0; i < 15000; ++i) {
        boundary[i] = '(';
    }
    for (int i = 15000; i < 30000; ++i) {
        boundary[i] = ')';
    }
    boundary[30000] = '\0';

    assert(longestValidParentheses(boundary) == 30000);

    return 0;
}