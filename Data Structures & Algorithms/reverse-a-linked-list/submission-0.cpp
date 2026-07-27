/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        if (head->next == nullptr) {
            return head;
        }
        //sol 1

        // ListNode* curr = head;
        // ListNode* nex = curr->next;
        // ListNode* prev = nullptr;
        // while (nex != nullptr) {
        //     curr->next = prev;
        //     prev = curr;
        //     curr = nex;
        //     nex = nex->next;
        // }
        // curr->next = prev;
        // return curr;

        //sol 2

        ListNode* curr = head;
        ListNode* prev = nullptr;

        while (curr != nullptr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};
