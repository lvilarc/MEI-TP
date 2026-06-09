#include <assert.h>
#include <limits.h>

int firstMissingPositive(int* nums, int numsSize);

int main(void) {
    {
        int nums[] = {1, 2, 0};
        assert(firstMissingPositive(nums, 3) == 3);
    }

    {
        int nums[] = {3, 4, -1, 1};
        assert(firstMissingPositive(nums, 4) == 2);
    }

    {
        int nums[] = {7, 8, 9, 11, 12};
        assert(firstMissingPositive(nums, 5) == 1);
    }

    {
        int nums[] = {1};
        assert(firstMissingPositive(nums, 1) == 2);
    }

    {
        int nums[] = {INT_MIN, INT_MAX, 2, 2, 1, 5, 3};
        assert(firstMissingPositive(nums, 7) == 4);
    }

    return 0;
}