class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # step 1: find all rotten oranges and all fresh oranges
        rotten = deque()
        fresh = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh.append((i,j))
        # step 2: for each currently rotten orange, see if it can turn any fresh orange
        count = 0
        len_fresh = len(fresh)
        new_rotten = deque()
        while fresh:
            count += 1
            while rotten:
                (i,j) = rotten.popleft()
                if (i-1, j) in fresh:
                    fresh.remove((i-1, j))
                    new_rotten.append((i-1, j))
                if (i+1, j) in fresh:
                    fresh.remove((i+1, j))
                    new_rotten.append((i+1, j))
                if (i, j-1) in fresh:
                    fresh.remove((i, j-1))
                    new_rotten.append((i, j-1))
                if (i, j+1) in fresh:
                    fresh.remove((i, j+1))
                    new_rotten.append((i, j+1))
            if len_fresh == len(fresh):
                return -1
            len_fresh = len(fresh)
            rotten = new_rotten
            new_rotten = deque()
        return count


        