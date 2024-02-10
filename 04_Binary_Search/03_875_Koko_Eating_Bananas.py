class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2 
            hours = 0
            for p in piles:
                hours += math.ceil(p/k) # we round up because we can only eat 1 pile per hour, we waste any remainder if we eat too fast.
            if hours <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
    
        return res

# Time complexity: 
# Space complexity: 

# Notes: 
# First thing to notice is that h >= len(p) otherwise we would not be able to finish all piles at any rate.
# Second thing to notice is that an upper bound for the solution is k <= max(piles), and we have to have a speed of at least 1.
# We then binary search through all of these values to find the value k where Koko can eat as slow as possible but finish all of the bananas within h.


