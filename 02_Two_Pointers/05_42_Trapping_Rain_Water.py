class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        rain_water = 0
        while l<r:
            # We want to increment whichever one is smallest as 
            # its the one that makes a difference to how much water we can fill in 
            # at this spot: min(left_max, right_max) - height[i]
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                rain_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                rain_water += right_max - height[r]

        return rain_water

# Time Complexity: O(n) - using two pointers method we only visit each element in the input array height once.
# Space Complexity: O(1) - we only store constants l, r, left_max, right_max.
