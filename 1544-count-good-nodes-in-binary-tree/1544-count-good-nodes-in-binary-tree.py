# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGood(root, root.val)
    def countGood(self, root, maxVal):
        if not root:
            return 0

        count = 0
        if root.val >= maxVal:
            count = 1
        
        maxVal = max(root.val, maxVal)

        count += self.countGood(root.left, maxVal)
        count += self.countGood(root.right, maxVal)

        return count
        