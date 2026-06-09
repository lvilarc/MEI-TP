#include <assert.h>
#include <stdio.h>

int findMin(int* nums, int numsSize);

int main(void) {
    int nums1[] = {1, 3, 5};
    assert(findMin(nums1, 3) == 1);

    int nums2[] = {2, 2, 2, 0, 1};
    assert(findMin(nums2, 5) == 0);

    int nums3[] = {1};
    assert(findMin(nums3, 1) == 1);

    int nums4[] = {3, 3, 3, 3, 3, 3, 3};
    assert(findMin(nums4, 7) == 3);

    int nums5[] = {10, 1, 10, 10, 10};
    assert(findMin(nums5, 5) == 1);

    printf("All tests passed.\n");
    return 0;
}