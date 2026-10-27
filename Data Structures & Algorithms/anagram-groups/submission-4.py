class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            c = [0]*26
            for l in s:
                c[ord(l)-ord('a')]+=1
            
            ana[tuple(c)].append(s)
        
        return [v for v in ana.values()]