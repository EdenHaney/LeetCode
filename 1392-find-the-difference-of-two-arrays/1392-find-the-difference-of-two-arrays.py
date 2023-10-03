class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer: [list, list] = [[], []]
        answer[0] = set(nums1) - set(nums2)
        answer[1] = set(nums2) - set(nums1)
        return answer
        