# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])
        while queue:
            right_most_node = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_most_node = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_most_node:
                result.append(right_most_node.val)

        return result