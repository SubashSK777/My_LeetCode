class Solution:
    def recoverFromPreorder(self, data):
        for count in range(100, 0, -1):
            data = data.replace("-" * count, chr(count + 65))

        def build_tree(parts, level):
            parts = parts.split(chr(level + 65))
            node = TreeNode(int(parts[0]))
            node.left = build_tree(parts[1], level + 1) if len(parts) > 1 else None
            node.right = build_tree(parts[2], level + 1) if len(parts) > 2 else None
            return node

        return build_tree(data, 1)