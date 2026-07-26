class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i <= j:
            l = s[i]
            r = s[j]
            if not l.isalnum():
                i+=1
                continue
            if not r.isalnum():
                j-=1
                continue
            if l.lower() == r.lower():
                i +=1
                j-=1
            else:
                return False
            
        return True
            