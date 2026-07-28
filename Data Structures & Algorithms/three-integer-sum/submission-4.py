class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                tot = nums[l]+nums[r]
                target = -nums[i]
                if tot == target:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < len(nums)-1 and nums[l+1] == nums[l]:
                        l+=1
                    l+=1
                    r-=1
                elif tot + nums[i] > 0:
                    r -=1
                else:
                    l +=1
        return res
                