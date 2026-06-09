#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool isNumber(char* s) {
    int i = 0, n = strlen(s);
    if (i < n && (s[i] == '+' || s[i] == '-')) i++;
    int digits = 0;
    while (i < n && isdigit((unsigned char)s[i])) { i++; digits++; }
    if (i < n && s[i] == '.') {
        i++;
        while (i < n && isdigit((unsigned char)s[i])) { i++; digits++; }
    }
    if (digits == 0) return false;
    if (i < n && (s[i] == 'e' || s[i] == 'E')) {
        i++;
        if (i < n && (s[i] == '+' || s[i] == '-')) i++;
        int ed = 0;
        while (i < n && isdigit((unsigned char)s[i])) { i++; ed++; }
        if (ed == 0) return false;
    }
    return i == n;
}
