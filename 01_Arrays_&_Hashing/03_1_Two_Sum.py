class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                return [nums_dict[target - nums[i]], i]
            nums_dict[nums[i]] = i

# Time complexity: O(N), where N is the length of nums. We only make one pass through nums.
# Space complexity: O(N). Storing each value num in the dict/hashmap.
