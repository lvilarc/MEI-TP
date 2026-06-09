#include <assert.h>
#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize);

int main(void) {
    {
        struct ListNode a3 = {5, NULL};
        struct ListNode a2 = {4, &a3};
        struct ListNode a1 = {1, &a2};

        struct ListNode b3 = {4, NULL};
        struct ListNode b2 = {3, &b3};
        struct ListNode b1 = {1, &b2};

        struct ListNode c2 = {6, NULL};
        struct ListNode c1 = {2, &c2};

        struct ListNode *lists[] = {&a1, &b1, &c1};
        struct ListNode *result = mergeKLists(lists, 3);
        int expected[] = {1, 1, 2, 3, 4, 4, 5, 6};

        for (int i = 0; i < 8; i++) {
            assert(result != NULL);
            assert(result->val == expected[i]);
            result = result->next;
        }
        assert(result == NULL);
    }

    {
        struct ListNode **lists = NULL;
        struct ListNode *result = mergeKLists(lists, 0);
        assert(result == NULL);
    }

    {
        struct ListNode *lists[] = {NULL};
        struct ListNode *result = mergeKLists(lists, 1);
        assert(result == NULL);
    }

    {
        struct ListNode a3 = {2, NULL};
        struct ListNode a2 = {-3, &a3};
        struct ListNode a1 = {-10, &a2};

        struct ListNode b4 = {4, NULL};
        struct ListNode b3 = {4, &b4};
        struct ListNode b2 = {0, &b3};
        struct ListNode b1 = {-3, &b2};

        struct ListNode c1 = {-5, NULL};

        struct ListNode *lists[] = {&a1, NULL, &b1, &c1};
        struct ListNode *result = mergeKLists(lists, 4);
        int expected[] = {-10, -5, -3, -3, 0, 2, 4, 4};

        for (int i = 0; i < 8; i++) {
            assert(result != NULL);
            assert(result->val == expected[i]);
            result = result->next;
        }
        assert(result == NULL);
    }

    {
        struct ListNode a1 = {-10000, NULL};
        struct ListNode b1 = {10000, NULL};
        struct ListNode c1 = {0, NULL};
        struct ListNode d1 = {-9999, NULL};
        struct ListNode e1 = {9999, NULL};

        struct ListNode *lists[] = {&a1, &b1, &c1, &d1, &e1};
        struct ListNode *result = mergeKLists(lists, 5);
        int expected[] = {-10000, -9999, 0, 9999, 10000};

        for (int i = 0; i < 5; i++) {
            assert(result != NULL);
            assert(result->val == expected[i]);
            result = result->next;
        }
        assert(result == NULL);
    }

    return 0;
}