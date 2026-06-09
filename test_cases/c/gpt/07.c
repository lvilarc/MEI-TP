#include <assert.h>
#include <stdbool.h>

bool isMatch(char *s, char *p);

int main(void) {
    char s1[] = "aa";
    char p1[] = "a";
    assert(isMatch(s1, p1) == false);

    char s2[] = "aa";
    char p2[] = "*";
    assert(isMatch(s2, p2) == true);

    char s3[] = "cb";
    char p3[] = "?a";
    assert(isMatch(s3, p3) == false);

    char s4[] = "";
    char p4[] = "";
    assert(isMatch(s4, p4) == true);

    char s5[2001];
    char p5[2001];
    for (int i = 0; i < 2000; i++) {
        s5[i] = 'a';
        p5[i] = '?';
    }
    s5[2000] = '\0';
    p5[2000] = '\0';
    assert(isMatch(s5, p5) == true);

    return 0;
}