# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def seqeseqe(root):
            if root != None:
            
                if root.right is None and root.left is None:
                    return [root.val]
                else:
                    l = seqeseqe(root.left)
                    r = seqeseqe(root.right)

                    return l + r
            else:
                return []
                

        return seqeseqe(root1) == seqeseqe(root2)