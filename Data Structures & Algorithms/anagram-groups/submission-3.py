class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for w in strs:
            counter = [0]*26
            for letter in w:
                counter[ord(letter)-ord('a')] +=1
            output[tuple(counter)].append(w)
        return list(output.values())