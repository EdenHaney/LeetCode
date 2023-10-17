class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # keeping track of where you've visited:
        # check if there are any O's around the border
        # if there is, check all adjacent fields for an "O", mark it as visited
        # continue until all adjacent O's are marked
        # flip all unvisited O's to X's
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def explore_adjacent(i, j):
            visited[i][j] = True
            if i+1 < len(board) and visited[i+1][j] is False and board[i+1][j] == "O":
                explore_adjacent(i+1, j)
            if i-1 >= 0 and visited[i-1][j] is False and board[i-1][j] == "O":
                explore_adjacent(i-1, j)
            if j+1 < len(board[0]) and visited[i][j+1] is False and board[i][j+1] == "O":
                explore_adjacent(i, j+1)
            if j-1 >= 0 and visited[i][j-1] is False and board[i][j-1] == "O":
                explore_adjacent(i, j-1)

        # visit edges first
        for i in range(len(board)):
            if i == 0 or i == len(board)-1:
                for j in range(len(board[0])):
                    if visited[i][j] is False and board[i][j] == "O":
                        explore_adjacent(i, j)
            else:
                for j in (0, len(board[0])-1):
                    if visited[i][j] is False and board[i][j] == "O":
                        explore_adjacent(i, j)

        # flip all remaining O's
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if visited[i][j] is False and board[i][j] == "O":
                    board[i][j] = "X"

        