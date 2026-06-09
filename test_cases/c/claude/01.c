#include <assert.h>
#include <math.h>
#include <stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size);

static int approx_equal(double a, double b) {
    return fabs(a - b) < 1e-5;
}

int main(void) {
    // Test 1: Example 1 - odd total length
    int a1[] = {1, 3};
    int b1[] = {2};
    assert(approx_equal(findMedianSortedArrays(a1, 2, b1, 1), 2.00000));

    // Test 2: Example 2 - even total length
    int a2[] = {1, 2};
    int b2[] = {3, 4};
    assert(approx_equal(findMedianSortedArrays(a2, 2, b2, 2), 2.50000));

    // Test 3: One array empty
    int b3[] = {1};
    assert(approx_equal(findMedianSortedArrays(NULL, 0, b3, 1), 1.00000));

    // Test 4: Negative numbers and different sizes
    int a4[] = {-5, -3, -1};
    int b4[] = {-2, 0, 2, 4};
    // merged: [-5,-3,-2,-1,0,2,4], median = -1
    assert(approx_equal(findMedianSortedArrays(a4, 3, b4, 4), -1.00000));

    // Test 5: Non-overlapping ranges, even total
    int a5[] = {1, 2, 3, 4};
    int b5[] = {5, 6, 7, 8};
    // merged: [1..8], median = (4+5)/2 = 4.5
    assert(approx_equal(findMedianSortedArrays(a5, 4, b5, 4), 4.50000));

    printf("All tests passed.\n");
    return 0;
}