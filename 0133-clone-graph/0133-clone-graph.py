"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        clones = {}
        clones[node.val] = Node(node.val, [])
        q = deque([node])

        while q:
            next_node = q.popleft()
            cur_clone = clones[next_node.val]            
            for neighbor in next_node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                cur_clone.neighbors.append(clones[neighbor.val])
        return clones[node.val]

        