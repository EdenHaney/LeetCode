# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 1
        sums = {}
        def dfs(node, level):
            if node is None:
                return
            if level in sums.keys():
                sums[level] += node.val
            else:
                sums[level] = node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return max(sums, key=sums.get)     
        
        