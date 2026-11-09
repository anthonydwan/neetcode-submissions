class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        i = 0 
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            t = 0 - nums[i]
            while l < r:
                lv, rv = nums[l], nums[r]
                if lv + rv == t:
                    output.append([nums[i],lv,rv])
                    l +=1
                    while l < len(nums)-1 and nums[l] == nums[l-1]:
                        l +=1
                    r -=1
                elif lv + rv < t:
                    l +=1
                else:
                    r -=1
        return output
                        

            