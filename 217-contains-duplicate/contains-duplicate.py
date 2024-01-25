class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for ele in nums:
            if ele not in hash:
                hash[ele] = 1
            else:
                return True
        return False