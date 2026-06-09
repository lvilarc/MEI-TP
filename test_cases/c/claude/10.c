#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

char ** fullJustify(char ** words, int wordsSize, int maxWidth, int* returnSize);

static void check(char **words, int wordsSize, int maxWidth, const char **expected, int expectedSize) {
    int returnSize = 0;
    char **result = fullJustify(words, wordsSize, maxWidth, &returnSize);
    assert(returnSize == expectedSize);
    for (int i = 0; i < expectedSize; i++) {
        assert(result[i] != NULL);
        assert((int)strlen(result[i]) == maxWidth);
        assert(strcmp(result[i], expected[i]) == 0);
    }
}

int main(void) {
    /* Test 1: Example 1 - normal case with multiple lines */
    {
        char *words[] = {"This", "is", "an", "example", "of", "text", "justification."};
        const char *expected[] = {
            "This    is    an",
            "example  of text",
            "justification.  "
        };
        check(words, 7, 16, expected, 3);
    }

    /* Test 2: Example 2 - line with a single word must be left-justified */
    {
        char *words[] = {"What", "must", "be", "acknowledgment", "shall", "be"};
        const char *expected[] = {
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        };
        check(words, 6, 16, expected, 3);
    }

    /* Test 3: Example 3 - uneven space distribution favors the left */
    {
        char *words[] = {"Science", "is", "what", "we", "understand", "well",
                         "enough", "to", "explain", "to", "a", "computer.",
                         "Art", "is", "everything", "else", "we", "do"};
        const char *expected[] = {
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        };
        check(words, 18, 20, expected, 6);
    }

    /* Test 4: Single word - must be left-justified and padded */
    {
        char *words[] = {"hello"};
        const char *expected[] = {
            "hello     "
        };
        check(words, 1, 10, expected, 1);
    }

    /* Test 5: Each word exactly fills the line width (boundary) */
    {
        char *words[] = {"abc", "def", "ghi"};
        const char *expected[] = {
            "abc",
            "def",
            "ghi"
        };
        check(words, 3, 3, expected, 3);
    }

    printf("All tests passed.\n");
    return 0;
}