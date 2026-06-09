#include <limits.h>

int maxProfit(int* prices, int n) {
    int buy1 = INT_MIN, sell1 = 0, buy2 = INT_MIN, sell2 = 0;
    for (int i = 0; i < n; i++) {
        int p = prices[i];
        if (-p > buy1) buy1 = -p;
        if (buy1 + p > sell1) sell1 = buy1 + p;
        if (sell1 - p > buy2) buy2 = sell1 - p;
        if (buy2 + p > sell2) sell2 = buy2 + p;
    }
    return sell2;
}
