"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_to_cnode = {}
        dummy_head = Node(x=0)
        c_node = dummy_head
        node = head
        while node:
            c_node.next = Node(node.val)
            node_to_cnode[node] = c_node.next
            node = node.next
            c_node = c_node.next
        
        node = head
        c_node = dummy_head.next
        while node:
            c_node.random = node_to_cnode.get(node.random)
            node = node.next
            c_node = c_node.next
            
        return dummy_head.next