#include <stdlib.h>
#include <string.h>

char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {
    char** res = malloc(sizeof(char*) * wordsSize);
    int lines = 0;
    int i = 0;
    while (i < wordsSize) {
        int j = i, lineLen = 0;
        while (j < wordsSize) {
            int wlen = strlen(words[j]);
            int needed = lineLen + wlen + (j - i); /* chars + new word + min gaps */
            if (needed > maxWidth) break;
            lineLen += wlen;
            j++;
        }
        int numWords = j - i;
        char* line = malloc(maxWidth + 1);
        memset(line, ' ', maxWidth);
        line[maxWidth] = '\0';
        int pos = 0;
        if (j == wordsSize || numWords == 1) {
            for (int w = i; w < j; w++) {
                int wl = strlen(words[w]);
                memcpy(line + pos, words[w], wl);
                pos += wl;
                if (w < j - 1) pos++; /* single space, already there */
            }
        } else {
            int totalSpaces = maxWidth - lineLen;
            int gaps = numWords - 1;
            int base = totalSpaces / gaps;
            int extra = totalSpaces % gaps;
            for (int w = i; w < j; w++) {
                int wl = strlen(words[w]);
                memcpy(line + pos, words[w], wl);
                pos += wl;
                if (w < j - 1) pos += base + ((w - i) < extra ? 1 : 0);
            }
        }
        res[lines++] = line;
        i = j;
    }
    *returnSize = lines;
    return res;
}
