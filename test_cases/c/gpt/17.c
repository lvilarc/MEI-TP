#include <assert.h>
#include <string.h>

int minCut(char* s);

int main(void) {
    char s1[] = "aab";
    assert(minCut(s1) == 1);

    char s2[] = "a";
    assert(minCut(s2) == 0);

    char s3[] = "ab";
    assert(minCut(s3) == 1);

    char s4[] = "abcde";
    assert(minCut(s4) == 4);

    char s5[2001];
    memset(s5, 'a', 2000);
    s5[2000] = '\0';
    assert(minCut(s5) == 0);

    return 0;
}