class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for n in nums:
            count[n] = count.get(n,0) + 1

        bucket = [[] for i in range(len(nums)+1)]
        

        for key,v in count.items():
            bucket[v].append(key)
        
        output = []

        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                output.append(n)
                if len(output) == k:
                    return output