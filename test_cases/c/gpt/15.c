#include <assert.h>
#include <string.h>

char*** findLadders(char* beginWord, char* endWord, char** wordList, int wordListSize, int* returnSize, int** returnColumnSizes);

int main(void) {
    {
        char w0[] = "hot";
        char w1[] = "dot";
        char w2[] = "dog";
        char w3[] = "lot";
        char w4[] = "log";
        char w5[] = "cog";
        char* wordList[] = {w0, w1, w2, w3, w4, w5};
        int returnSize = 0;
        int* returnColumnSizes = 0;

        char*** result = findLadders("hit", "cog", wordList, 6, &returnSize, &returnColumnSizes);

        assert(returnSize == 2);
        assert(result != 0);
        assert(returnColumnSizes != 0);

        int found1 = 0;
        int found2 = 0;

        for (int i = 0; i < returnSize; i++) {
            assert(returnColumnSizes[i] == 5);

            if (strcmp(result[i][0], "hit") == 0 &&
                strcmp(result[i][1], "hot") == 0 &&
                strcmp(result[i][2], "dot") == 0 &&
                strcmp(result[i][3], "dog") == 0 &&
                strcmp(result[i][4], "cog") == 0) {
                assert(!found1);
                found1 = 1;
            } else if (strcmp(result[i][0], "hit") == 0 &&
                       strcmp(result[i][1], "hot") == 0 &&
                       strcmp(result[i][2], "lot") == 0 &&
                       strcmp(result[i][3], "log") == 0 &&
                       strcmp(result[i][4], "cog") == 0) {
                assert(!found2);
                found2 = 1;
            } else {
                assert(0);
            }
        }

        assert(found1);
        assert(found2);
    }

    {
        char w0[] = "hot";
        char w1[] = "dot";
        char w2[] = "dog";
        char w3[] = "lot";
        char w4[] = "log";
        char* wordList[] = {w0, w1, w2, w3, w4};
        int returnSize = 0;
        int* returnColumnSizes = 0;

        char*** result = findLadders("hit", "cog", wordList, 5, &returnSize, &returnColumnSizes);

        assert(returnSize == 0);
        (void)result;
    }

    {
        char w0[] = "c";
        char* wordList[] = {w0};
        int returnSize = 0;
        int* returnColumnSizes = 0;

        char*** result = findLadders("a", "c", wordList, 1, &returnSize, &returnColumnSizes);

        assert(returnSize == 1);
        assert(result != 0);
        assert(returnColumnSizes != 0);
        assert(returnColumnSizes[0] == 2);
        assert(strcmp(result[0][0], "a") == 0);
        assert(strcmp(result[0][1], "c") == 0);
    }

    {
        char w0[] = "ted";
        char w1[] = "tex";
        char w2[] = "red";
        char w3[] = "tax";
        char w4[] = "tad";
        char w5[] = "den";
        char w6[] = "rex";
        char w7[] = "pee";
        char* wordList[] = {w0, w1, w2, w3, w4, w5, w6, w7};
        int returnSize = 0;
        int* returnColumnSizes = 0;

        char*** result = findLadders("red", "tax", wordList, 8, &returnSize, &returnColumnSizes);

        assert(returnSize == 3);
        assert(result != 0);
        assert(returnColumnSizes != 0);

        int found1 = 0;
        int found2 = 0;
        int found3 = 0;

        for (int i = 0; i < returnSize; i++) {
            assert(returnColumnSizes[i] == 4);

            if (strcmp(result[i][0], "red") == 0 &&
                strcmp(result[i][1], "ted") == 0 &&
                strcmp(result[i][2], "tad") == 0 &&
                strcmp(result[i][3], "tax") == 0) {
                assert(!found1);
                found1 = 1;
            } else if (strcmp(result[i][0], "red") == 0 &&
                       strcmp(result[i][1], "ted") == 0 &&
                       strcmp(result[i][2], "tex") == 0 &&
                       strcmp(result[i][3], "tax") == 0) {
                assert(!found2);
                found2 = 1;
            } else if (strcmp(result[i][0], "red") == 0 &&
                       strcmp(result[i][1], "rex") == 0 &&
                       strcmp(result[i][2], "tex") == 0 &&
                       strcmp(result[i][3], "tax") == 0) {
                assert(!found3);
                found3 = 1;
            } else {
                assert(0);
            }
        }

        assert(found1);
        assert(found2);
        assert(found3);
    }

    {
        char w0[] = "baaaa";
        char w1[] = "bbaaa";
        char w2[] = "bbbaa";
        char w3[] = "bbbba";
        char w4[] = "bbbbb";
        char* wordList[] = {w0, w1, w2, w3, w4};
        int returnSize = 0;
        int* returnColumnSizes = 0;

        char*** result = findLadders("aaaaa", "bbbbb", wordList, 5, &returnSize, &returnColumnSizes);

        assert(returnSize == 1);
        assert(result != 0);
        assert(returnColumnSizes != 0);
        assert(returnColumnSizes[0] == 6);
        assert(strcmp(result[0][0], "aaaaa") == 0);
        assert(strcmp(result[0][1], "baaaa") == 0);
        assert(strcmp(result[0][2], "bbaaa") == 0);
        assert(strcmp(result[0][3], "bbbaa") == 0);
        assert(strcmp(result[0][4], "bbbba") == 0);
        assert(strcmp(result[0][5], "bbbbb") == 0);
    }

    return 0;
}