#include <assert.h>

int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize);

int main(void) {
    {
        char beginWord[] = "hit";
        char endWord[] = "cog";
        char w0[] = "hot";
        char w1[] = "dot";
        char w2[] = "dog";
        char w3[] = "lot";
        char w4[] = "log";
        char w5[] = "cog";
        char* wordList[] = {w0, w1, w2, w3, w4, w5};

        assert(ladderLength(beginWord, endWord, wordList, 6) == 5);
    }

    {
        char beginWord[] = "hit";
        char endWord[] = "cog";
        char w0[] = "hot";
        char w1[] = "dot";
        char w2[] = "dog";
        char w3[] = "lot";
        char w4[] = "log";
        char* wordList[] = {w0, w1, w2, w3, w4};

        assert(ladderLength(beginWord, endWord, wordList, 5) == 0);
    }

    {
        char beginWord[] = "hit";
        char endWord[] = "hot";
        char w0[] = "hot";
        char* wordList[] = {w0};

        assert(ladderLength(beginWord, endWord, wordList, 1) == 2);
    }

    {
        char beginWord[] = "hit";
        char endWord[] = "cog";
        char w0[] = "hot";
        char w1[] = "dot";
        char w2[] = "tod";
        char w3[] = "cog";
        char* wordList[] = {w0, w1, w2, w3};

        assert(ladderLength(beginWord, endWord, wordList, 4) == 0);
    }

    {
        char beginWord[] = "a";
        char endWord[] = "c";
        char w0[] = "b";
        char w1[] = "c";
        char* wordList[] = {w0, w1};

        assert(ladderLength(beginWord, endWord, wordList, 2) == 2);
    }

    return 0;
}