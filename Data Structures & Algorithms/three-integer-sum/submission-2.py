class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    r = r-1
                    while nums[l] == nums[l-1] and l < r:
                        l = l +1
                elif nums[i] + nums[l] + nums[r]  < 0:
                    l = l+1
                else:
                    r = r-1
        return triplets