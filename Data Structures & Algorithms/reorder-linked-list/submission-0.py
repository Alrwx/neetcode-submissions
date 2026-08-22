# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #the middle + 1 will be the second half, the head is the first half
        l1 = head
        l2 = slow.next

        #reverse the second half of the list
        prev = slow.next = None

        while l2:
            temp = l2.next
            l2.next = prev

            prev = l2
            l2 = temp

        #alternate the appendings
        l2 = prev
        while l1 and l2:
            #preserving the next of the first list
            temp1 = l1.next
            l1.next = l2
            l1 = temp1

            temp2 = l2.next
            l2.next = l1
            l2 = temp2

        # return head


