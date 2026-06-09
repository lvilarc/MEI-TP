#include <assert.h>
#include <stdio.h>

int maxProfit(int* prices, int pricesSize);

int main(void) {
    int p1[] = {3, 3, 5, 0, 0, 3, 1, 4};
    assert(maxProfit(p1, 8) == 6);

    int p2[] = {1, 2, 3, 4, 5};
    assert(maxProfit(p2, 5) == 4);

    int p3[] = {7, 6, 4, 3, 1};
    assert(maxProfit(p3, 5) == 0);

    int p4[] = {5};
    assert(maxProfit(p4, 1) == 0);

    int p5[] = {1, 5, 2, 8, 3, 10};
    assert(maxProfit(p5, 6) == 14);

    printf("All tests passed.\n");
    return 0;
}