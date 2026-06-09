#include <stdlib.h>
#include <string.h>

int longestValidParentheses(char* s) {
    int n = strlen(s);
    int max = 0;
    int* st = malloc(sizeof(int) * (n + 1));
    int top = 0;
    st[top++] = -1;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            st[top++] = i;
        } else {
            top--;
            if (top == 0) {
                st[top++] = i;
            } else {
                int len = i - st[top - 1];
                if (len > max) max = len;
            }
        }
    }
    free(st);
    return max;
}
