# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        max_twin_sum  = 0
        curr_left, curr_right = prev, slow
        while curr_left and slow:
            twin_sum = curr_left.val + curr_right.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            curr_left = curr_left.next
            curr_right = curr_right.next
        
        return max_twin_sum
