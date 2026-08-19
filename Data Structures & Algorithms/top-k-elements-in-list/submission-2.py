class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq =[[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0) # for each number in input nums, check if that number is already counted and add 1 to that
                                        # after looping the result will be count = {1:1, 2:2, 3:1} etc
        for n , c in count.items():
            freq[c].append(n) # n occurs c times ie if nums = 1 and it occrs 1 time, then the freq list under index 1 will be turned to 1
        res= []
        # print
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




