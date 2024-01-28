class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        freq = [(-1*value, key) for key, value in Counter(nums).items()]
        heapq.heapify(freq)

        out = []
        for i in range(k):
            out.append(heapq.heappop(freq)[-1])
        return out

        