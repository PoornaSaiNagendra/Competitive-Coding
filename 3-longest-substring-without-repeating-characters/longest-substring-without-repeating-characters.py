class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        unique_chars = {}
        length_so_far = 0
        start = -1
        for index, char in enumerate(s):
            if char in unique_chars and unique_chars[char] > start:
                start = unique_chars[char]
            unique_chars[char] = index
            length_so_far = max(length_so_far, index - start)
        return length_so_far

        
        