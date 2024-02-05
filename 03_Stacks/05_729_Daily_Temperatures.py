class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        stack = [] # [(index, temp)]

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stack_index, stack_temperature = stack.pop()
                answer[stack_index] = i - stack_index
            stack.append((i, temperature))

        return answer

# Time complexity: O(N) - only visit each element once.
# Space complexity: O(N) - in case we have to store entire list of temperatures in case of monotonically decreasing sequence.
