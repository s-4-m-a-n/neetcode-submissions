# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result
            
        queue = deque([[root, 0]])

        while queue:
            node, level = queue.popleft()
            
            if len(result) == level:
                result.append([node.val])
            else:
                result[-1].append(node.val)

            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
            

        return result