class Solution:
    def countBits(self, n: int) -> List[int]:
      list_ones = [0]
      for i in range(1, n+1):
        num_ones = list_ones[i >> 1] + (i & 1)
        list_ones.append(num_ones)
      return list_ones