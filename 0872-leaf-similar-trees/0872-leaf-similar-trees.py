# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
     
class Solution:
    def get_leaves(self, root: Optional[TreeNode]) -> List[int]:
        leaves = []
        if root is None:
            return []
        if root.left is None and root.right is None:
            leaves.append(root.val)
        self.get_leaves(root.left)
        self.get_leaves(root.right)
        return leaves + self.get_leaves(root.left) + self.get_leaves(root.right)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaves(root1) == self.get_leaves(root2)

        