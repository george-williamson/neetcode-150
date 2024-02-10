class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target: l = m + 1
            elif nums[m] > target: r = m - 1
            else: return m
        return -1

# Time complexity: O(log(N)) - we cut the lists space in half each time. So the worst case is how many times do we need to divide the list by two to end up with 1 element left. 
# 1 = N / 2^X
# 2^X = N
# log2(N) = X
# So we have to divide through log(N) times to get left with 1.
    
# Space complexity: O(1) - we don't need to hold any values in memory.
