class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        count = 0
        
        def explore_island(i: int, j: int):
            print(f"count: {count}, ({i}, {j})")
            visited[i][j] = True
            if i+1 < len(grid) and grid[i+1][j] == '1' and visited[i+1][j] is False:
                explore_island(i+1, j)
            if i-1 >= 0 and grid[i-1][j] == '1' and visited[i-1][j] is False:
                explore_island(i-1, j)
            if j+1 < len(grid[0]) and grid[i][j+1] == '1' and visited[i][j+1] is False:
                explore_island(i, j+1)
            if j-1 >= 0 and grid[i][j-1] == '1' and visited[i][j-1] is False:
                explore_island(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] is False:
                    count += 1
                    explore_island(i, j)
    

        return count