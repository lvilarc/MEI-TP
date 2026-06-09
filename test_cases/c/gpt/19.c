#include <assert.h>
#include <string.h>

char** wordBreak(char* s, char** wordDict, int wordDictSize, int* returnSize);

int main(void) {
    {
        char s[] = "catsanddog";
        char* wordDict[] = {"cat", "cats", "and", "sand", "dog"};
        char* expected[] = {"cats and dog", "cat sand dog"};
        int returnSize = -1;
        char** result = wordBreak(s, wordDict, 5, &returnSize);

        assert(returnSize == 2);
        for (int i = 0; i < 2; i++) {
            int found = 0;
            for (int j = 0; j < returnSize; j++) {
                if (strcmp(result[j], expected[i]) == 0) {
                    found = 1;
                    break;
                }
            }
            assert(found);
        }
    }

    {
        char s[] = "pineapplepenapple";
        char* wordDict[] = {"apple", "pen", "applepen", "pine", "pineapple"};
        char* expected[] = {
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple"
        };
        int returnSize = -1;
        char** result = wordBreak(s, wordDict, 5, &returnSize);

        assert(returnSize == 3);
        for (int i = 0; i < 3; i++) {
            int found = 0;
            for (int j = 0; j < returnSize; j++) {
                if (strcmp(result[j], expected[i]) == 0) {
                    found = 1;
                    break;
                }
            }
            assert(found);
        }
    }

    {
        char s[] = "catsandog";
        char* wordDict[] = {"cats", "dog", "sand", "and", "cat"};
        int returnSize = -1;
        char** result = wordBreak(s, wordDict, 5, &returnSize);

        (void)result;
        assert(returnSize == 0);
    }

    {
        char s[] = "a";
        char* wordDict[] = {"a"};
        char* expected[] = {"a"};
        int returnSize = -1;
        char** result = wordBreak(s, wordDict, 1, &returnSize);

        assert(returnSize == 1);
        assert(strcmp(result[0], expected[0]) == 0);
    }

    {
        char s[] = "aaaaaaaaaaaaaaaaaaaa";
        char* wordDict[] = {"aaaaaaaaaa"};
        char* expected[] = {"aaaaaaaaaa aaaaaaaaaa"};
        int returnSize = -1;
        char** result = wordBreak(s, wordDict, 1, &returnSize);

        assert(returnSize == 1);
        assert(strcmp(result[0], expected[0]) == 0);
    }

    return 0;
}