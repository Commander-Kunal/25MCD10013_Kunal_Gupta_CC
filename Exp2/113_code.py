class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, current_path, remaining_sum):
            if not node:
                return
            
            # Include the current node in the path
            current_path.append(node.val)
            
            # Check if it's a leaf node and the target sum is met
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(current_path)) # Append a copy of the path
            else:
                # Recurse on left and right subtrees
                dfs(node.left, current_path, remaining_sum - node.val)
                dfs(node.right, current_path, remaining_sum - node.val)
                
            # Backtrack: remove the current node before going back up
            current_path.pop()
            
        dfs(root, [], targetSum)
        return result
