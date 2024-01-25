class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for ele in strs:
            word = ''.join(sorted(ele))
            if word not in hash:
                hash[word] = []
            hash[word].append(ele)
        
        return list(hash.values())