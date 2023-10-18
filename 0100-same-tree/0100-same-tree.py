# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q = []
        q_q = []
        if p:
            p_q.append(p)
        if q:
            q_q.append(q)
        while p_q and q_q:
            p_node = p_q.pop(0)
            q_node = q_q.pop(0)
            if p_node.val != q_node.val:
                return False
            if p_node.left and q_node.left:
                p_q.append(p_node.left)
                q_q.append(q_node.left)
            elif p_node.left or q_node.left:
                return False
            if p_node.right and q_node.right:
                p_q.append(p_node.right)
                q_q.append(q_node.right)
            elif p_node.right or q_node.right:
                return False 
        if len(p_q) != len(q_q):
            return False    
        return True
        