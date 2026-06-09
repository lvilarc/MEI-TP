#include <stdlib.h>
#include <string.h>

static char* dupstr(const char* str) {
    size_t n = strlen(str) + 1;
    char* p = malloc(n);
    memcpy(p, str, n);
    return p;
}

static char** g_res;
static int g_cnt, g_cap;

static void add(const char* str) {
    if (g_cnt == g_cap) {
        g_cap *= 2;
        g_res = realloc(g_res, sizeof(char*) * g_cap);
    }
    g_res[g_cnt++] = dupstr(str);
}

static int inDict(const char* word, int wl, char** dict, int n) {
    for (int i = 0; i < n; i++)
        if ((int)strlen(dict[i]) == wl && strncmp(word, dict[i], wl) == 0) return 1;
    return 0;
}

static void dfs(char* s, int start, int slen, char** dict, int dn, char* buf, int buflen) {
    if (start == slen) {
        buf[buflen - 1] = '\0'; /* drop trailing space */
        add(buf);
        return;
    }
    for (int end = start + 1; end <= slen; end++) {
        int wl = end - start;
        if (inDict(s + start, wl, dict, dn)) {
            memcpy(buf + buflen, s + start, wl);
            buf[buflen + wl] = ' ';
            dfs(s, end, slen, dict, dn, buf, buflen + wl + 1);
        }
    }
}

char** wordBreak(char* s, char** wordDict, int wordDictSize, int* returnSize) {
    g_cnt = 0;
    g_cap = 16;
    g_res = malloc(sizeof(char*) * g_cap);
    int slen = strlen(s);
    char* buf = malloc(slen * 2 + 2);
    dfs(s, 0, slen, wordDict, wordDictSize, buf, 0);
    free(buf);
    *returnSize = g_cnt;
    return g_res;
}
