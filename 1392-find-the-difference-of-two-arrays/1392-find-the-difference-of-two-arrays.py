class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer: [list, list] = [[], []]
        for num in nums1:
            if num not in answer[0]:
                answer[0].append(num)
        for num in nums2:
            if num in nums1:
                if num in answer[0]:
                    answer[0].remove(num)
            elif num not in answer[1]:
                answer[1].append(num)
        return answer
        