# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([[root, 0]])

        while queue:
            node, level = queue.popleft()
            
            if not node:
                continue

            if len(result) == level:
                result.append([node.val])
            else:
                result[-1].append(node.val)

            queue.append([node.left, level+1])
            queue.append([node.right, level+1])
            

        return result