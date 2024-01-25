class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        # nums.sort()
        for i, ele in enumerate(nums):
            comp = target - ele
            if comp in hash:
                return [hash[comp], i]
            else:
                hash[ele] = i
        