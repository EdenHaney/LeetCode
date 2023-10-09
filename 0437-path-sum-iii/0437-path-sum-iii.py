# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count_paths = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.dfs(root, targetSum, True)
        return self.count_paths

    def dfs(self, root: TreeNode, cur_sum: int, new: bool): 
        if not root:
            return

        next_sum = cur_sum - root.val
        if next_sum==0:
            self.count_paths +=1

        self.dfs(root.left, next_sum, False)
        self.dfs(root.right, next_sum, False)

        if new: 
            self.dfs(root.left, self.targetSum, True)
            self.dfs(root.right, self.targetSum, True)
