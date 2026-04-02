# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        notes: 
        - considering the preorder traversal restriction,
        it's just going to be DFS.
        """
        preorderList = [] # list of TreeNodes
        def preorder(curr):
            if not curr:
                return
            preorderList.append(curr)
            preorder(curr.left)
            preorder(curr.right)
            return
        preorder(root)
        # at this point, preorderList should be filled
        # ex: (1), (2), (3), (4), (5), (6)
        dummy = root
        i = 1
        while i < len(preorderList) and dummy:
            dummy.right = preorderList[i]
            dummy.left = None
            dummy = dummy.right
            i += 1
