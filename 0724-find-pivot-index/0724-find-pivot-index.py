class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:len(nums)])
        if left_sum == right_sum:
            return 0
        index = 1
        while index < len(nums):
            print(left_sum)
            print(right_sum)
            left_sum += nums[index -1]
            right_sum -= nums[index]
            if left_sum == right_sum:
                return index
            index += 1
        return -1
