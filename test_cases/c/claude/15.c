#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char ***findLadders(char *beginWord, char *endWord, char **wordList, int wordListSize,
                    int *returnSize, int **returnColumnSizes);

static int cmp_str(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

static int cmp_seq(const void *a, const void *b) {
    char **sa = *(char ***)a;
    char **sb = *(char ***)b;
    int i = 0;
    while (sa[i] && sb[i]) {
        int c = strcmp(sa[i], sb[i]);
        if (c != 0) return c;
        i++;
    }
    return 0;
}

static int seq_contains(char ***seqs, int n, int seqLen, char **target) {
    for (int i = 0; i < n; i++) {
        int match = 1;
        for (int j = 0; j < seqLen; j++) {
            if (strcmp(seqs[i][j], target[j]) != 0) { match = 0; break; }
        }
        if (match) return 1;
    }
    return 0;
}

int main(void) {
    /* Test 1: classic example with 2 shortest sequences */
    {
        char *beginWord = "hit";
        char *endWord = "cog";
        char *wordList[] = {"hot", "dot", "dog", "lot", "log", "cog"};
        int returnSize = 0;
        int *returnColumnSizes = NULL;
        char ***result = findLadders(beginWord, endWord, wordList, 6, &returnSize, &returnColumnSizes);
        assert(returnSize == 2);
        for (int i = 0; i < returnSize; i++) assert(returnColumnSizes[i] == 5);
        char *exp1[] = {"hit", "hot", "dot", "dog", "cog"};
        char *exp2[] = {"hit", "hot", "lot", "log", "cog"};
        assert(seq_contains(result, returnSize, 5, exp1));
        assert(seq_contains(result, returnSize, 5, exp2));
    }

    /* Test 2: endWord not in wordList -> empty */
    {
        char *beginWord = "hit";
        char *endWord = "cog";
        char *wordList[] = {"hot", "dot", "dog", "lot", "log"};
        int returnSize = -1;
        int *returnColumnSizes = NULL;
        findLadders(beginWord, endWord, wordList, 5, &returnSize, &returnColumnSizes);
        assert(returnSize == 0);
    }

    /* Test 3: single-step transformation */
    {
        char *beginWord = "a";
        char *endWord = "c";
        char *wordList[] = {"a", "b", "c"};
        int returnSize = 0;
        int *returnColumnSizes = NULL;
        char ***result = findLadders(beginWord, endWord, wordList, 3, &returnSize, &returnColumnSizes);
        assert(returnSize == 1);
        assert(returnColumnSizes[0] == 2);
        assert(strcmp(result[0][0], "a") == 0);
        assert(strcmp(result[0][1], "c") == 0);
    }

    /* Test 4: no path exists at all (disconnected) */
    {
        char *beginWord = "hot";
        char *endWord = "dog";
        char *wordList[] = {"hot", "dog"};
        int returnSize = -1;
        int *returnColumnSizes = NULL;
        findLadders(beginWord, endWord, wordList, 2, &returnSize, &returnColumnSizes);
        assert(returnSize == 0);
    }

    /* Test 5: multiple equal-length paths, longer words */
    {
        char *beginWord = "red";
        char *endWord = "tax";
        char *wordList[] = {"ted", "tex", "red", "tax", "tad", "den", "rex", "pee"};
        int returnSize = 0;
        int *returnColumnSizes = NULL;
        char ***result = findLadders(beginWord, endWord, wordList, 8, &returnSize, &returnColumnSizes);
        assert(returnSize == 3);
        for (int i = 0; i < returnSize; i++) assert(returnColumnSizes[i] == 4);
        char *e1[] = {"red", "ted", "tad", "tax"};
        char *e2[] = {"red", "ted", "tex", "tax"};
        char *e3[] = {"red", "rex", "tex", "tax"};
        assert(seq_contains(result, returnSize, 4, e1));
        assert(seq_contains(result, returnSize, 4, e2));
        assert(seq_contains(result, returnSize, 4, e3));
    }

    printf("All tests passed!\n");
    return 0;
}