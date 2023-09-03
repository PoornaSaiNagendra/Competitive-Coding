class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [False]*(len(nums))
        suffix_product = [False]*(len(nums))
        product = 1

        for index in range(len(nums)):
            prefix_product[index] = product
            product *= nums[index]

        product = 1
        for index in range(len(nums) - 1, -1, -1):
            suffix_product[index] = product
            product *= nums[index]

        for index in range(len(prefix_product)):
            prefix_product[index] *= suffix_product[index]
        
        return prefix_product

