# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #theres a midpoint present where we split between n-1 and the index itself
        #we can find the midpoint via slow fast pointers

        if not head or not head.next:
            return

        slow = head
        fast = slow.next # so its 1 ahead and slow lags behind

        #find the midpoint here
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at the midpoint where we start caring about\
        #reverse the linked list:
        prev = slow
        curr = slow.next
        prev.next = None

        while curr:
            #preserve our next
            tmp = curr.next
            #update our next
            curr.next = prev
            #update vars
            prev = curr
            curr = tmp

        start = head
        ends = prev

        while start != None:
            #preserve our next elements
            snext = start.next
            lnext = ends.next
            start.next = ends
            ends.next = snext

            start = snext
            ends = lnext
    
        return
