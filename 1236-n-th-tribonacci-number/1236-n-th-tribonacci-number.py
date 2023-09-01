class Solution:
    def tribonacci(self, n: int) -> int:
        d = [0, 1, 1]
        if n == 0:
            return 0
        for i in range(3, n+1):
            d.append(sum(d))
            d.pop(0)
        return d[2]