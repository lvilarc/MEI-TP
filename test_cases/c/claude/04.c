#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* findSubstring(char* s, char** words, int wordsSize, int* returnSize);

static int cmp_int(const void* a, const void* b) {
    int ia = *(const int*)a;
    int ib = *(const int*)b;
    return (ia > ib) - (ia < ib);
}

static int arrays_equal(int* a, int a_size, int* expected, int expected_size) {
    if (a_size != expected_size) return 0;
    if (a_size == 0) return 1;
    qsort(a, a_size, sizeof(int), cmp_int);
    qsort(expected, expected_size, sizeof(int), cmp_int);
    for (int i = 0; i < a_size; i++) {
        if (a[i] != expected[i]) return 0;
    }
    return 1;
}

int main(void) {
    /* Test 1: Example 1 - basic case */
    {
        char s[] = "barfoothefoobarman";
        char* words[] = {"foo", "bar"};
        int returnSize = 0;
        int* result = findSubstring(s, words, 2, &returnSize);
        int expected[] = {0, 9};
        assert(arrays_equal(result, returnSize, expected, 2));
        free(result);
    }

    /* Test 2: Example 2 - no matches with repeated words */
    {
        char s[] = "wordgoodgoodgoodbestword";
        char* words[] = {"word", "good", "best", "word"};
        int returnSize = 0;
        int* result = findSubstring(s, words, 4, &returnSize);
        assert(returnSize == 0);
        free(result);
    }

    /* Test 3: Example 3 - three words multiple matches */
    {
        char s[] = "barfoofoobarthefoobarman";
        char* words[] = {"bar", "foo", "the"};
        int returnSize = 0;
        int* result = findSubstring(s, words, 3, &returnSize);
        int expected[] = {6, 9, 12};
        assert(arrays_equal(result, returnSize, expected, 3));
        free(result);
    }

    /* Test 4: Edge case - single word, single occurrence */
    {
        char s[] = "a";
        char* words[] = {"a"};
        int returnSize = 0;
        int* result = findSubstring(s, words, 1, &returnSize);
        int expected[] = {0};
        assert(arrays_equal(result, returnSize, expected, 1));
        free(result);
    }

    /* Test 5: Boundary - string shorter than concatenated words length */
    {
        char s[] = "ab";
        char* words[] = {"abc", "def"};
        int returnSize = 0;
        int* result = findSubstring(s, words, 2, &returnSize);
        assert(returnSize == 0);
        free(result);
    }

    printf("All tests passed!\n");
    return 0;
}