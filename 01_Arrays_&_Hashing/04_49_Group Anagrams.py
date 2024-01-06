class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return anagrams.values()

# Time Complexity: O(N*K*log(K)), where N is the length of strs, K is the length of the word. 
# Space Complexity: O(N*K)
