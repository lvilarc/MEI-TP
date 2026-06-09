#include <assert.h>
#include <stdio.h>

int ladderLength(char *beginWord, char *endWord, char **wordList, int wordListSize);

int main(void) {
    /* Test 1: Standard case with valid transformation */
    char *wordList1[] = {"hot", "dot", "dog", "lot", "log", "cog"};
    assert(ladderLength("hit", "cog", wordList1, 6) == 5);

    /* Test 2: endWord not in wordList */
    char *wordList2[] = {"hot", "dot", "dog", "lot", "log"};
    assert(ladderLength("hit", "cog", wordList2, 5) == 0);

    /* Test 3: Direct one-letter transformation */
    char *wordList3[] = {"bat"};
    assert(ladderLength("cat", "bat", wordList3, 1) == 2);

    /* Test 4: No possible transformation, isolated words */
    char *wordList4[] = {"xyz", "abc"};
    assert(ladderLength("cat", "dog", wordList4, 2) == 0);

    /* Test 5: Single character words */
    char *wordList5[] = {"b", "c", "d"};
    assert(ladderLength("a", "c", wordList5, 3) == 2);

    printf("All tests passed!\n");
    return 0;
}