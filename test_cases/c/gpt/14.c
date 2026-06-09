#include <assert.h>

int maxProfit(int* prices, int pricesSize);

int main(void) {
    int prices1[] = {3, 3, 5, 0, 0, 3, 1, 4};
    assert(maxProfit(prices1, 8) == 6);

    int prices2[] = {1, 2, 3, 4, 5};
    assert(maxProfit(prices2, 5) == 4);

    int prices3[] = {7, 6, 4, 3, 1};
    assert(maxProfit(prices3, 5) == 0);

    int prices4[] = {5};
    assert(maxProfit(prices4, 1) == 0);

    int prices5[] = {0, 100000, 0, 100000};
    assert(maxProfit(prices5, 4) == 200000);

    return 0;
}