#include <assert.h>
#include <stdio.h>

int firstMissingPositive(int* nums, int numsSize);

int main(void) {
    int nums1[] = {1, 2, 0};
    assert(firstMissingPositive(nums1, 3) == 3);

    int nums2[] = {3, 4, -1, 1};
    assert(firstMissingPositive(nums2, 4) == 2);

    int nums3[] = {7, 8, 9, 11, 12};
    assert(firstMissingPositive(nums3, 5) == 1);

    int nums4[] = {1};
    assert(firstMissingPositive(nums4, 1) == 2);

    int nums5[] = {2147483647, -2147483648, 1, 2, 3};
    assert(firstMissingPositive(nums5, 5) == 4);

    printf("All tests passed!\n");
    return 0;
}