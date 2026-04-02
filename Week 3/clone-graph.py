"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
"""
1: 2,4 ||| 2: 1, 3 ||| 3: 2, 4 ||| 4: 1, 3
recreate current node -> then recursively create the current node's neighbor nodes, essentially
performing a DFS (create 1 -> then 2 -> then 3 -> then 4, based on the mapping 2 lines above)
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None # nothing to copy
        oldToNew = {}
        def copy(curr):
            if curr in oldToNew:
                return oldToNew[curr] # already built this new node
            root = Node(curr.val)
            oldToNew[curr] = root
            for neighbor in curr.neighbors:
                root.neighbors.append(copy(neighbor))
            return root
        return copy(node) # -> should return copy of current node
