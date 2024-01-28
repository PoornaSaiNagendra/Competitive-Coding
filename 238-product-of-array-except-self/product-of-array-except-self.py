class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N, MUL = len(nums), 1
        out = [1]*N
        for i in range(1, N):
            MUL *= nums[i-1]
            out[i] = MUL
        MUL = 1
        for i in range(N-2, -1, -1):
            MUL *= nums[i+1]
            out[i] *= MUL
        return out

