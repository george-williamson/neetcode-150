class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {']':'[', ')':'(', '}':'{'}
        stack = []
        for b in s:
            if b in bracket_map:
                if stack and stack[-1] == bracket_map[b]: stack.pop()
                else: return False
            else: stack.append(b)
        return False if stack else True

# Time complexity: O(n) we visit every element in the input string exactly once.
# Space complexity: O(n) we will need to be able to store every element in the input string in the stack. E.g. if input string is all open brackets.

# Notes: The return statement catches the edge case where we are left with open brackets in the stack and run out of characters to find corresponding closed brackets.
            
