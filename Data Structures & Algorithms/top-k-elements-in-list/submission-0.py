class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # do a bucket sort where we know the number of frequency is max the same number as the len of list

        c = {}
        freq = [[] for i in range(len(nums)+1)]


        for n in nums:
            c[n] = 1 + c.get(n, 0)
        
        for n,i in c.items():
            freq[i].append(n)

        output = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output