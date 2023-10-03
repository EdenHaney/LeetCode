class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        next = -1
        count = 1
        for i in range(2, n+1):
            if intervals[-i][1] <= intervals[next][0]:
                next = -i
                count+= 1
        return n - count
