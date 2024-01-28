class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1
        heap = []
        for key, value in freq_table.items():
            if len(heap) >= k: # If size is k then we dont want to increase the size further 
                heappushpop(heap, (value, key))
            elif len(heap) < k: # Size is not k then freely push values
                heappush(heap, (value, key))
		# After this operation the heap contains only k largest values of all the values in nums
        out = []
        for i in range(k):
            out.append(heappop(heap)[1])
        return out

        