class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # how many ways can we organize m-1 objects of type down and n-1 objects of type right?
        # (m-1+n-1)!/(m-1)!(n-1)!
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
        