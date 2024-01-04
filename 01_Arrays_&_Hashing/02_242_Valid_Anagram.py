class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = defaultdict(int)

        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1

        if all(v == 0 for v in counts.values()): return True
