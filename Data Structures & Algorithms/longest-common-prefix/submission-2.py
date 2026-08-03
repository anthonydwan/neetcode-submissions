class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return res
            letter = strs[0][i]
            for word in strs:
                if len(word) <= i or word[i] != letter:
                    return res
            i +=1
            res += letter