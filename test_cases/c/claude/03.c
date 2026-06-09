#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize);

static struct ListNode* buildList(int* arr, int n) {
    if (n == 0) return NULL;
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->val = arr[0];
    head->next = NULL;
    struct ListNode* cur = head;
    for (int i = 1; i < n; i++) {
        cur->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        cur->next->val = arr[i];
        cur->next->next = NULL;
        cur = cur->next;
    }
    return head;
}

static void verifyList(struct ListNode* head, int* expected, int n) {
    struct ListNode* cur = head;
    for (int i = 0; i < n; i++) {
        assert(cur != NULL);
        assert(cur->val == expected[i]);
        cur = cur->next;
    }
    assert(cur == NULL);
}

int main(void) {
    /* Test 1: Normal case from example 1 */
    {
        int a1[] = {1, 4, 5};
        int a2[] = {1, 3, 4};
        int a3[] = {2, 6};
        struct ListNode* lists[3];
        lists[0] = buildList(a1, 3);
        lists[1] = buildList(a2, 3);
        lists[2] = buildList(a3, 3);
        int expected[] = {1, 1, 2, 3, 4, 4, 5, 6};
        struct ListNode* result = mergeKLists(lists, 3);
        verifyList(result, expected, 8);
    }

    /* Test 2: Empty array of lists (k == 0) */
    {
        struct ListNode* result = mergeKLists(NULL, 0);
        assert(result == NULL);
    }

    /* Test 3: Single empty list */
    {
        struct ListNode* lists[1];
        lists[0] = NULL;
        struct ListNode* result = mergeKLists(lists, 1);
        assert(result == NULL);
    }

    /* Test 4: Single non-empty list */
    {
        int a1[] = {-3, 0, 2, 5};
        struct ListNode* lists[1];
        lists[0] = buildList(a1, 4);
        int expected[] = {-3, 0, 2, 5};
        struct ListNode* result = mergeKLists(lists, 1);
        verifyList(result, expected, 4);
    }

    /* Test 5: Mix of empty and non-empty lists with negative and boundary values */
    {
        int a1[] = {-10000, 0, 10000};
        int a3[] = {-5000, -1, 1, 9999};
        struct ListNode* lists[4];
        lists[0] = buildList(a1, 3);
        lists[1] = NULL;
        lists[2] = buildList(a3, 4);
        lists[3] = NULL;
        int expected[] = {-10000, -5000, -1, 0, 1, 9999, 10000};
        struct ListNode* result = mergeKLists(lists, 4);
        verifyList(result, expected, 7);
    }

    printf("All tests passed!\n");
    return 0;
}