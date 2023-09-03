class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        if len(numbers) < 2:
            return out
        start, end = 0, len(numbers) - 1
        # 2, 4, 5, 7, 13, 15
        # 12
        while start < end:
            temp = numbers[start] + numbers[end]
            if temp > target:
                end -= 1
            elif temp < target:
                start += 1
            elif temp == target:
                break
        out = [start + 1, end + 1]
        return out