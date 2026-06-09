#include <assert.h>
#include <stdio.h>

int longestValidParentheses(char* s);

int main(void) {
    assert(longestValidParentheses("(()") == 2);
    assert(longestValidParentheses(")()())") == 4);
    assert(longestValidParentheses("") == 0);
    assert(longestValidParentheses("()(()") == 2);
    assert(longestValidParentheses("()(())") == 6);
    return 0;
}