class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
    
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: continue
            # Two Sum
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0: r -= 1
                elif three_sum < 0: l += 1
                else: 
                    result.append([a, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]: l+=1
        return result

# Time complexity: O(n^2) - We sort the list which is O(nlogn), and we also have a nested loop where the first loop fixes a
# and traverses the list. The second loop essentially performs Two Sum with a sorted array, so O(n*n) = O(n^2). O(n^2) + O(nlogn) = O(n^2)
# as quadratic time is a greater upper bound.

# Space complexity: O(n) - We need to store the sorted list which O(n)as Python uses Timsort for sorting arrays which has O(n) space complexity.



