class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+": stack.append(stack.pop()+stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif t == "*": stack.append(stack.pop()*stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else: stack.append(int(t))
        return stack[-1]

# Time complexity: O(n) - we visit every element in tokens once.
# Space complexity: O(n) - in the case all inputs are operands (numbers), we will have to store all in the stack.

    
