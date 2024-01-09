class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s))+"#"+s for s in strs)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result

  # Time complexity: O(n) - we iterate through nums once O(n) as well as the encoding string O(n), O(n) + O(n) = O(n).
  # Space complexity: O(n) - we need to make a temporary store of the encoding which is the length of strs.
