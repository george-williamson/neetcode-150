class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create hash set to get unique values
        n_set = set(nums)
        longest_sequence = 0
        # For each number check if its the start of a sequence
        for n in nums:
            length = 0
            if (n-1) not in n_set:
                # If we find the start of a sequence check if the next number is 
                # in the hash set. Increment length to keep track of the sequence length
                while (n+length) in n_set:
                    length +=1
            longest_sequence = max(longest_sequence, length)
        return longest_sequence

# Time complexity: O(n), we run through the list of numbers only once. Checking sequences once a start has been found is O(1).
# Space complexity: O(n), we store the distinct values in nums as a hashset. 
# Getting rid of duplicates is key because the existence of duplicates can drastically increase the runtime for test cases with many duplicates, due to the repeated work done.
