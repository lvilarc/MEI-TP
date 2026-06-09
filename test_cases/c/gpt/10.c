#include <assert.h>
#include <string.h>

char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize);

int main(void) {
    {
        char* words[] = {"This", "is", "an", "example", "of", "text", "justification."};
        char* expected[] = {
            "This    is    an",
            "example  of text",
            "justification.  "
        };
        int returnSize = 0;
        char** result = fullJustify(words, 7, 16, &returnSize);

        assert(returnSize == 3);
        for (int i = 0; i < returnSize; i++) {
            assert(strcmp(result[i], expected[i]) == 0);
        }
    }

    {
        char* words[] = {"What", "must", "be", "acknowledgment", "shall", "be"};
        char* expected[] = {
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        };
        int returnSize = 0;
        char** result = fullJustify(words, 6, 16, &returnSize);

        assert(returnSize == 3);
        for (int i = 0; i < returnSize; i++) {
            assert(strcmp(result[i], expected[i]) == 0);
        }
    }

    {
        char* words[] = {
            "Science", "is", "what", "we", "understand", "well", "enough",
            "to", "explain", "to", "a", "computer.", "Art", "is",
            "everything", "else", "we", "do"
        };
        char* expected[] = {
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        };
        int returnSize = 0;
        char** result = fullJustify(words, 18, 20, &returnSize);

        assert(returnSize == 6);
        for (int i = 0; i < returnSize; i++) {
            assert(strcmp(result[i], expected[i]) == 0);
        }
    }

    {
        char* words[] = {"a", "b", "c", "d"};
        char* expected[] = {
            "a  b c",
            "d     "
        };
        int returnSize = 0;
        char** result = fullJustify(words, 4, 6, &returnSize);

        assert(returnSize == 2);
        for (int i = 0; i < returnSize; i++) {
            assert(strcmp(result[i], expected[i]) == 0);
        }
    }

    {
        char* words[] = {"a", "b", "c"};
        char* expected[] = {
            "a",
            "b",
            "c"
        };
        int returnSize = 0;
        char** result = fullJustify(words, 3, 1, &returnSize);

        assert(returnSize == 3);
        for (int i = 0; i < returnSize; i++) {
            assert(strcmp(result[i], expected[i]) == 0);
        }
    }

    return 0;
}