#include <assert.h>

int findMin(int* nums, int numsSize);

int main(void) {
    int nums1[] = {1, 3, 5};
    assert(findMin(nums1, 3) == 1);

    int nums2[] = {2, 2, 2, 0, 1};
    assert(findMin(nums2, 5) == 0);

    int nums3[] = {-5000};
    assert(findMin(nums3, 1) == -5000);

    int nums4[] = {7, 7, 7, 7, 7};
    assert(findMin(nums4, 5) == 7);

    int nums5[5000];
    for (int i = 0; i < 2500; i++) {
        nums5[i] = 5000;
    }
    for (int i = 2500; i < 5000; i++) {
        nums5[i] = -5000;
    }
    assert(findMin(nums5, 5000) == -5000);

    return 0;
}