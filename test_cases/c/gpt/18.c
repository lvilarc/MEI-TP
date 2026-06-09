#include <assert.h>

int candy(int* ratings, int ratingsSize);

int main(void) {
    int ratings1[] = {1, 0, 2};
    assert(candy(ratings1, 3) == 5);

    int ratings2[] = {1, 2, 2};
    assert(candy(ratings2, 3) == 4);

    int ratings3[] = {5};
    assert(candy(ratings3, 1) == 1);

    int ratings4[] = {1, 3, 4, 5, 2};
    assert(candy(ratings4, 5) == 11);

    static int ratings5[20000];
    for (int i = 0; i < 20000; i++) {
        ratings5[i] = i;
    }
    assert(candy(ratings5, 20000) == 200010000);

    return 0;
}