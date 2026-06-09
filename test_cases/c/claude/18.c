#include <stdio.h>
#include <assert.h>

int candy(int* ratings, int ratingsSize);

int main(void) {
    int t1[] = {1, 0, 2};
    assert(candy(t1, 3) == 5);

    int t2[] = {1, 2, 2};
    assert(candy(t2, 3) == 4);

    int t3[] = {5};
    assert(candy(t3, 1) == 1);

    int t4[] = {1, 2, 3, 4, 5};
    assert(candy(t4, 5) == 15);

    int t5[] = {1, 3, 4, 5, 2};
    assert(candy(t5, 5) == 11);

    printf("All tests passed.\n");
    return 0;
}