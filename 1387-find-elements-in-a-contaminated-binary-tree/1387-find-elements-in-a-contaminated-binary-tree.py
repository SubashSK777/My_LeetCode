# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.s = set([0])

        root.val = 0
        q = deque([root])
        
        while q:
            node = q.popleft()
            self.s.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
                q.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                q.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)