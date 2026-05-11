class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        top_k = sorted(
            freq_map.items(),
            key=lambda item: item[1],
            reverse=True
        )[:k]

        return [num for num, count in top_k]