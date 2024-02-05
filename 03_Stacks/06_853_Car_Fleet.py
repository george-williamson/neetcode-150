class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        position_speed = [(p,s) for p,s in zip(position, speed)]

        for p, s in sorted(position_speed, key=lambda x: x[0])[::-1]:
            time = (target-p)/s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]: stack.pop()
        return len(stack)

  # Time complexity: O(nlogn) - we need a sorted list for this to work.
  # Space complexity: O(n) - in case no cars intersect and we need to store all cars in the stack as separate fleets.
