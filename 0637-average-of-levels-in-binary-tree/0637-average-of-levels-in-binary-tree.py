# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        q = []
        q.append(root)
        averages = []
        while q:
            total = 0
            count = 0
            for i in range(len(q)):
                next_node = q.pop(0)
                if next_node:
                    total += next_node.val
                    count += 1
                    q.append(next_node.left)
                    q.append(next_node.right)
            if count > 0:
                averages.append(total/count)

        return averages
                
        