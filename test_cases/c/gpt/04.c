#include <assert.h>
#include <stdlib.h>

int* findSubstring(char* s, char** words, int wordsSize, int* returnSize);

int main(void) {
    int returnSize;
    int* result;

    {
        char s[] = "barfoothefoobarman";
        char* words[] = {"foo", "bar"};
        result = findSubstring(s, words, 2, &returnSize);

        assert(returnSize == 2);
        assert((result[0] == 0 || result[1] == 0));
        assert((result[0] == 9 || result[1] == 9));

        free(result);
    }

    {
        char s[] = "wordgoodgoodgoodbestword";
        char* words[] = {"word", "good", "best", "word"};
        result = findSubstring(s, words, 4, &returnSize);

        assert(returnSize == 0);

        free(result);
    }

    {
        char s[] = "barfoofoobarthefoobarman";
        char* words[] = {"bar", "foo", "the"};
        result = findSubstring(s, words, 3, &returnSize);

        assert(returnSize == 3);
        assert((result[0] == 6 || result[1] == 6 || result[2] == 6));
        assert((result[0] == 9 || result[1] == 9 || result[2] == 9));
        assert((result[0] == 12 || result[1] == 12 || result[2] == 12));

        free(result);
    }

    {
        char s[] = "wordgoodgoodgoodbestword";
        char* words[] = {"word", "good", "best", "good"};
        result = findSubstring(s, words, 4, &returnSize);

        assert(returnSize == 1);
        assert(result[0] == 8);

        free(result);
    }

    {
        char s[] = "a";
        char* words[] = {"a"};
        result = findSubstring(s, words, 1, &returnSize);

        assert(returnSize == 1);
        assert(result[0] == 0);

        free(result);
    }

    return 0;
}