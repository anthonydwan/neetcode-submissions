class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_c = [0]*26
        t_c = [0]*26
        for l in s:
            s_c[ord(l)-ord('a')] +=1
        for l in t:
            t_c[ord(l)-ord('a')] +=1
        return t_c == s_c