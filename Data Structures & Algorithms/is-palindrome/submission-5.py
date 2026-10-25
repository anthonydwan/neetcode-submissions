class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1
        while l < r:
            lc = s[l]
            rc = s[r]
            if not lc.isalnum():
                l+=1
                continue
            if not rc.isalnum():
                r -=1
                continue
            if lc.lower() != rc.lower():
                return False
            else:
                l+=1
                r-=1
        
        return True
                