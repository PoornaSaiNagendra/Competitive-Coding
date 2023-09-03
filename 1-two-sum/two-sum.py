class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        if len(nums) < 2:
            return out
        
        num_index = {}

        for index, num in enumerate(nums):
            pair = (target - num)
            if pair in num_index:
                out = [num_index[pair], index]
            else:
                num_index[num] = index
        return out
        