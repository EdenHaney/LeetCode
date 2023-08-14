# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def __init__(self):
        # self.sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # recurse tree and update sum with any values within range
        add = 0
        if root is None:
            return 0
        if root.val >= low and root.val <= high:
            add = root.val
        return add + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        