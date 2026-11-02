class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        # Sort the basket positions
        position.sort()
        
        # Helper function to check if we can place m balls with at least min_dist apart
        def can_place(min_dist):
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = position[i]
                    if count >= m:
                        return True
            return False

        # Binary search range for the minimum magnetic force
        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                ans = mid          # Valid force, try for a larger one
                left = mid + 1
            else:
                right = mid - 1    # Too large, try a smaller force

        return ans
