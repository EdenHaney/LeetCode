class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dupes = []
        for i in nums:
            if i in dupes:
                dupes.remove(i)
            else:
                dupes.append(i)
        return dupes[0]
      
        