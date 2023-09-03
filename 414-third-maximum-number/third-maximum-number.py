class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        minheap=[]
        taken = {}

        for num in nums:
            if num in taken:
                continue
            if len(minheap) == 3:
                if minheap[0] < num:
                    del taken[minheap[0]]
                    heappop(minheap)

                    heappush(minheap, num)
                    taken[num] = 1
            else:
                taken[num] = 1
                heappush(minheap, num)

        if len(minheap) == 1:
            return minheap[0]
        elif len(minheap) == 2:
            return max(minheap[0], minheap[1])
        return minheap[0]
        
