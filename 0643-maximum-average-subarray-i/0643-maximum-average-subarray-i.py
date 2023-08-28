class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # go through all subarrays and find max average val
        added = sum(nums[0:k])
        max_val = added
        for i in range(0,len(nums)-k):
            added = added - nums[i] + nums[i+k]
            if added > max_val:
                max_val = added
        return max_val/k