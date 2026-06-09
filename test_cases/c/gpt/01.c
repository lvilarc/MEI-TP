#include <assert.h>
#include <math.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size);

int main(void) {
    const double EPS = 1e-9;

    {
        int nums1[] = {1, 3};
        int nums2[] = {2};
        double result = findMedianSortedArrays(nums1, 2, nums2, 1);
        assert(fabs(result - 2.0) < EPS);
    }

    {
        int nums1[] = {1, 2};
        int nums2[] = {3, 4};
        double result = findMedianSortedArrays(nums1, 2, nums2, 2);
        assert(fabs(result - 2.5) < EPS);
    }

    {
        int nums2[] = {1};
        double result = findMedianSortedArrays(NULL, 0, nums2, 1);
        assert(fabs(result - 1.0) < EPS);
    }

    {
        int nums1[] = {-5, -3, -1};
        int nums2[] = {-4, -2, 0};
        double result = findMedianSortedArrays(nums1, 3, nums2, 3);
        assert(fabs(result - (-2.5)) < EPS);
    }

    {
        int nums1[] = {-1000000, 1000000};
        int nums2[] = {-1000000, 1000000};
        double result = findMedianSortedArrays(nums1, 2, nums2, 2);
        assert(fabs(result - 0.0) < EPS);
    }

    return 0;
}