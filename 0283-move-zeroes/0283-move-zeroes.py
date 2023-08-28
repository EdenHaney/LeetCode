class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current element is non-zero, swap it with the element at index
                # This effectively moves non-zero elements to the beginning of the list
                nums[i], nums[index] = nums[index], nums[i]
                index += 1 
                