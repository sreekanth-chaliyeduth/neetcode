from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Time Complexity: O(n log k)
        # Space Complexity: O(n)

        freq_map = Counter(nums)

        top_k = heapq.nlargest(
            k,
            freq_map.keys(),
            key=freq_map.get
        )

        return top_k