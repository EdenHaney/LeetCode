# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def isGood(self, root: TreeNode, largest_val: int) -> int:
        if root is None:
            return 0
        count = 0
        if largest_val <= root.val:
            largest_val = root.val
            count = 1
        return count + self.isGood(root.left, largest_val) + self.isGood(root.right, largest_val)
            
    def goodNodes(self, root: TreeNode) -> int:
        return self.isGood(root, -inf)
        
            
        