class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1]*len(nums), [1]*len(nums)
        N = len(nums)
        for i in range(1, N):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[N - i - 1] = suffix[N - i] * nums[N - i]
        out = []
        for i in range(N):
            out.append(prefix[i]*suffix[i])
        return out
