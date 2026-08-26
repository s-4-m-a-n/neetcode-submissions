# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(node1, node2):
            if not node1 and not node2:
                return True
            
            if node1 and node2 and node1.val == node2.val:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
            
            return False
        
        stack = [(root, subRoot)]
        while stack:
            r, s = stack.pop()
            is_same = isSame(r, s)
            if is_same:
                return True
            if r.left:
                stack.append((r.left, subRoot))
            if r.right:
                stack.append((r.right, subRoot))
        return False