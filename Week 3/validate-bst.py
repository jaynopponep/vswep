class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # traverse the BFS way
        def BFS(l,m_node,r):
            if not m_node:
                return True
            if (not l < m_node.val) or (not m_node.val < r):
                return False
            return BFS(l, m_node.left, m_node.val) and BFS(m_node.val, m_node.right, r)
        # traverse the DFS way
        return BFS(float('-inf'), root, float('inf'))
