#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

char** wordBreak(char* s, char** wordDict, int wordDictSize, int* returnSize);

static int contains(char** arr, int n, const char* target) {
    for (int i = 0; i < n; i++) {
        if (strcmp(arr[i], target) == 0) return 1;
    }
    return 0;
}

static void free_result(char** result, int size) {
    if (!result) return;
    for (int i = 0; i < size; i++) free(result[i]);
    free(result);
}

int main(void) {
    /* Test 1: Example 1 - "catsanddog" -> 2 sentences */
    {
        char s[] = "catsanddog";
        char* dict[] = {"cat", "cats", "and", "sand", "dog"};
        int returnSize = 0;
        char** result = wordBreak(s, dict, 5, &returnSize);
        assert(returnSize == 2);
        assert(contains(result, returnSize, "cats and dog"));
        assert(contains(result, returnSize, "cat sand dog"));
        free_result(result, returnSize);
    }

    /* Test 2: Example 2 - "pineapplepenapple" -> 3 sentences */
    {
        char s[] = "pineapplepenapple";
        char* dict[] = {"apple", "pen", "applepen", "pine", "pineapple"};
        int returnSize = 0;
        char** result = wordBreak(s, dict, 5, &returnSize);
        assert(returnSize == 3);
        assert(contains(result, returnSize, "pine apple pen apple"));
        assert(contains(result, returnSize, "pineapple pen apple"));
        assert(contains(result, returnSize, "pine applepen apple"));
        free_result(result, returnSize);
    }

    /* Test 3: Example 3 - "catsandog" -> no valid segmentation */
    {
        char s[] = "catsandog";
        char* dict[] = {"cats", "dog", "sand", "and", "cat"};
        int returnSize = 0;
        char** result = wordBreak(s, dict, 5, &returnSize);
        assert(returnSize == 0);
        free_result(result, returnSize);
    }

    /* Test 4: Boundary - single character string matching single word in dict */
    {
        char s[] = "a";
        char* dict[] = {"a"};
        int returnSize = 0;
        char** result = wordBreak(s, dict, 1, &returnSize);
        assert(returnSize == 1);
        assert(contains(result, returnSize, "a"));
        free_result(result, returnSize);
    }

    /* Test 5: Edge case - repeated reuse of the same word */
    {
        char s[] = "aaaa";
        char* dict[] = {"a", "aa"};
        int returnSize = 0;
        char** result = wordBreak(s, dict, 2, &returnSize);
        /* Possible segmentations:
           "a a a a", "a a aa", "a aa a", "aa a a", "aa aa" -> 5 */
        assert(returnSize == 5);
        assert(contains(result, returnSize, "a a a a"));
        assert(contains(result, returnSize, "a a aa"));
        assert(contains(result, returnSize, "a aa a"));
        assert(contains(result, returnSize, "aa a a"));
        assert(contains(result, returnSize, "aa aa"));
        free_result(result, returnSize);
    }

    printf("All tests passed.\n");
    return 0;
}