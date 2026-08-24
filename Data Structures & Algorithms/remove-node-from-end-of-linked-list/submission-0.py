# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #heres the plan

        #2 pointers, 1 dummy for the case its the first element
        #we want the fast to be ahead of the slow by n
        #then we iterate both till fast is at the end

        #this makes slow at the n+1 position from the end of the list
        #then we just delete that

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for i in range(n):
            fast = fast.next
        # fast is n spaces ahead of slow

        #now fast is at null, slow is n+1 spaces away from null
        while fast:
            slow = slow.next
            fast = fast.next

        #we skip over the next node

        slow.next = slow.next.next
        

        #this will be the head of the updated list
        return dummy.next










        # fast = head

        # #fast is n spaces in front of slow
        # for i in range(n):
        #     fast = fast.next

        # dummy = ListNode(0, head)
        # slow = dummy

        # #go to the very end
        # while fast:
        #     slow = slow.next
        #     fast = fast.next

        # #delete the next element
        # slow.next = slow.next.next

        # return dummy.next
