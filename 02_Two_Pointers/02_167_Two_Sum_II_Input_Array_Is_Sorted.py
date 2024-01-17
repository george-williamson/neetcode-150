class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            left_right_sum = numbers[l] + numbers[r]
            if left_right_sum > target: r -= 1
            if left_right_sum < target: l += 1
            if left_right_sum == target: return [l+1, r+1]

# Time complexity: O(n) - Only traverses the entire input array at most once.
# Space complexity: O(1) - We don't use any additional memory in this process, just the input.
