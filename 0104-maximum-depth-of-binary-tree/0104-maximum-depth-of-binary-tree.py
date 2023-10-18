# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current_depth = 0
        q = []
        if root:
            q.append(root)
        while q:
            current_depth += 1
            for i in range(len(q)):
                next_node = q.pop(0)
                l = next_node.left
                if l:
                    q.append(l)
                r = next_node.right
                if r:
                    q.append(r)       
        return current_depth 