#include <stdlib.h>
#include <string.h>

static char* dupstr(const char* str) {
    size_t n = strlen(str) + 1;
    char* p = malloc(n);
    memcpy(p, str, n);
    return p;
}

static int diffByOne(const char* a, const char* b) {
    int d = 0;
    for (int i = 0; a[i]; i++) {
        if (a[i] != b[i]) { d++; if (d > 1) return 0; }
    }
    return d == 1;
}

/* path collection */
static int*** g_paths;   /* not used; we collect index paths */
static int** g_idxPaths;
static int* g_idxLens;
static int g_cnt, g_cap;

static void record(int* stack, int depth) {
    if (g_cnt == g_cap) {
        g_cap *= 2;
        g_idxPaths = realloc(g_idxPaths, sizeof(int*) * g_cap);
        g_idxLens = realloc(g_idxLens, sizeof(int) * g_cap);
    }
    int* p = malloc(sizeof(int) * depth);
    /* stack holds path from end down to begin; reverse it */
    for (int i = 0; i < depth; i++) p[i] = stack[depth - 1 - i];
    g_idxPaths[g_cnt] = p;
    g_idxLens[g_cnt] = depth;
    g_cnt++;
}

static void dfs(int cur, int begin, int** parents, int* parentCnt,
                int* stack, int depth) {
    stack[depth] = cur;
    depth++;
    if (cur == begin) {
        record(stack, depth);
    } else {
        for (int k = 0; k < parentCnt[cur]; k++)
            dfs(parents[cur][k], begin, parents, parentCnt, stack, depth);
    }
}

char*** findLadders(char* beginWord, char* endWord, char** wordList,
                    int wordListSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    *returnColumnSizes = NULL;

    /* node 0 = beginWord, nodes 1.. = wordList (skip dup of beginWord) */
    int N = 1;
    char** node = malloc(sizeof(char*) * (wordListSize + 1));
    node[0] = beginWord;
    int endIdx = -1;
    if (strcmp(beginWord, endWord) == 0) endIdx = 0;
    for (int i = 0; i < wordListSize; i++) {
        if (strcmp(wordList[i], beginWord) == 0) continue;
        node[N] = wordList[i];
        if (endIdx == -1 && strcmp(wordList[i], endWord) == 0) endIdx = N;
        N++;
    }
    if (endIdx == -1) { free(node); return NULL; }

    /* BFS from node 0, building parents (predecessors on shortest paths) */
    int* dist = malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++) dist[i] = -1;
    int** parents = malloc(sizeof(int*) * N);
    int* parentCnt = malloc(sizeof(int) * N);
    int* parentCap = malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++) { parents[i] = NULL; parentCnt[i] = 0; parentCap[i] = 0; }

    int* queue = malloc(sizeof(int) * N);
    int qh = 0, qt = 0;
    dist[0] = 0;
    queue[qt++] = 0;
    int found = 0;
    while (qh < qt && !found) {
        int levelSize = qt - qh;
        /* process one level; mark nodes discovered this level so multiple
           parents at the same previous level are all recorded */
        int* discovered = malloc(sizeof(int) * N);
        int dc = 0;
        for (int s = 0; s < levelSize; s++) {
            int u = queue[qh++];
            for (int v = 0; v < N; v++) {
                if (v == u) continue;
                if (!diffByOne(node[u], node[v])) continue;
                if (dist[v] == -1) {
                    if (dist[v] == -1) {
                        /* will set distance below after collecting */
                    }
                    if (parentCnt[v] == 0 && parentCap[v] == 0) {
                        parentCap[v] = 4;
                        parents[v] = malloc(sizeof(int) * parentCap[v]);
                    }
                    if (parentCnt[v] == parentCap[v]) {
                        parentCap[v] *= 2;
                        parents[v] = realloc(parents[v], sizeof(int) * parentCap[v]);
                    }
                    /* only add as parent if not already, and v is one level below u */
                    parents[v][parentCnt[v]++] = u;
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        discovered[dc++] = v;
                    }
                } else if (dist[v] == dist[u] + 1) {
                    if (parentCnt[v] == parentCap[v]) {
                        parentCap[v] *= 2;
                        parents[v] = realloc(parents[v], sizeof(int) * parentCap[v]);
                    }
                    parents[v][parentCnt[v]++] = u;
                }
            }
        }
        /* enqueue newly discovered nodes for the next level */
        for (int i = 0; i < dc; i++) {
            queue[qt++] = discovered[i];
            if (discovered[i] == endIdx) found = 1;
        }
        free(discovered);
    }

    char*** result = NULL;
    if (dist[endIdx] != -1) {
        g_cnt = 0; g_cap = 16;
        g_idxPaths = malloc(sizeof(int*) * g_cap);
        g_idxLens = malloc(sizeof(int) * g_cap);
        int* stack = malloc(sizeof(int) * (dist[endIdx] + 1));
        dfs(endIdx, 0, parents, parentCnt, stack, 0);
        free(stack);

        result = malloc(sizeof(char**) * g_cnt);
        *returnColumnSizes = malloc(sizeof(int) * g_cnt);
        for (int i = 0; i < g_cnt; i++) {
            int len = g_idxLens[i];
            result[i] = malloc(sizeof(char*) * len);
            (*returnColumnSizes)[i] = len;
            for (int j = 0; j < len; j++) {
                result[i][j] = dupstr(node[g_idxPaths[i][j]]);
            }
            free(g_idxPaths[i]);
        }
        *returnSize = g_cnt;
        free(g_idxPaths);
        free(g_idxLens);
    }

    for (int i = 0; i < N; i++) free(parents[i]);
    free(parents); free(parentCnt); free(parentCap);
    free(dist); free(queue); free(node);
    (void)g_paths;
    return result;
}
