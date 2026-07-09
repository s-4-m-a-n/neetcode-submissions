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
        node = head
        while node:
            node_to_cnode[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            copy = node_to_cnode.get(node)
            copy.next = node_to_cnode.get(node.next)
            copy.random = node_to_cnode.get(node.random)
            node = node.next
        return node_to_cnode.get(head)
