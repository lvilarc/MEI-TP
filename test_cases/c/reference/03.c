#include <stddef.h>

struct ListNode { int val; struct ListNode *next; };

struct ListNode* mergeKLists(struct ListNode** lists, int k) {
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* tail = &dummy;
    while (1) {
        int best = -1;
        for (int i = 0; i < k; i++) {
            if (lists[i] && (best == -1 || lists[i]->val < lists[best]->val))
                best = i;
        }
        if (best == -1) break;
        tail->next = lists[best];
        tail = lists[best];
        lists[best] = lists[best]->next;
    }
    tail->next = NULL;
    return dummy.next;
}
