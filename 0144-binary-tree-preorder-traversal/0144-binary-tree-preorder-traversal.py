class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            dfs(node.left)           # Traverse left subtree
            dfs(node.right)          # Traverse right subtree
        
        dfs(root)
        return result