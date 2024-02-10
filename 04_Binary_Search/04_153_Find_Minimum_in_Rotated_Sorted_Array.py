class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = (l + r) // 2
            res = min(nums[l], res)
            if nums[m] >= nums[l]: l = m + 1
            else: r = m

        return res

# Time complexity: O(log(N)) - it's just binary search.
# Space complexity: O(1) - No memory needed other than constants.

# Notes:
# The key is to spot that essentially we now have two sorted sub arrays in the array nums.
# If we find that the middle value is greater or equal to what's at the left pointer, given the array is sorted it means that we won't find a minimum to the left.
# Therefore we want to search on the right (e.g. 4 5 6 7 if the pointer is at 7 we can cancel out everythign to the left). Otherwise we want to search on the left
# because the middle value is less than what is on the left meaning that the minimum point is somewhere to the left.
