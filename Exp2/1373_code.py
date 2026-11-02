class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 1, float('inf'), float('-inf'), 0
            
            l_bst, l_min, l_max, l_sum = dfs(node.left)
            r_bst, r_min, r_max, r_sum = dfs(node.right)
            
            if l_bst and r_bst and l_max < node.val < r_min:
                current_sum = l_sum + r_sum + node.val
                max_sum = max(max_sum, current_sum)
                
                current_min = min(l_min, node.val)
                current_max = max(r_max, node.val)
                return 1, current_min, current_max, current_sum
            
            return 0, 0, 0, 0

        dfs(root)
        return max_sum
