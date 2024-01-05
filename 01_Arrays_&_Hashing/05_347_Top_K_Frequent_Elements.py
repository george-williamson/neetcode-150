class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums: counts[num] += 1
        return [tup[0] for tup in sorted(counts.items(), key=lambda x: -x[1])][:k]
