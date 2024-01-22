class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0
        while l < r:
            width = r-l
            smallest_height = min(height[l], height[r])
            container_height = smallest_height*width
            if container_height > water: water = container_height
            if height[l] < height[r]: l+=1
            else: r-=1
        return water

# Time complexity: O(n) - using two pointers we visit each element in the list of heights at most once.
# Space complexity: O(1) - we store the two constants of smallest_height and the current heighest container.

