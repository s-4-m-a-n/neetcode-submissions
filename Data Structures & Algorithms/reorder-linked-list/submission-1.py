# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # find the center
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # rever the other half
        second = slow.next
        prev = None    
        slow.next = None    
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # reorder
        left = head
        right = prev
        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next
            left = left_next
            right = right_next



