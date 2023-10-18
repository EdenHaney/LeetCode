# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = []
        r = []
        if root:
            l.append(root.left)
            r.append(root.right)
        else: 
            return True

        while l and r:
            left_node = l.pop(0)
            right_node = r.pop(0)
            if left_node and right_node:
                if left_node.val != right_node.val:
                    print("a")
                    return False
                l.append(left_node.left)
                l.append(left_node.right)
                r.append(right_node.right)
                r.append(right_node.left)
            elif left_node or right_node:
                print("b")
                return False
        return len(l) == len(r)
        