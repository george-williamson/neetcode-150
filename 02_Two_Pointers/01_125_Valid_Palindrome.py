class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointers at either end of the string
        l, r = 0, len(s)-1
        # Iterate through the string from either side
        # Only check alphanumeric characters
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

# Time complexity: O(n) - We just loop through the array once essentially half and half from either side.
# Space complexity: O(1) - We do not need to use any additional memory.


        
