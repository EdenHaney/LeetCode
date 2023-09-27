class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # find every exit and the number of steps to the exit
        # shortest path to each available cell
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        entrance = (entrance[0],entrance[1])
        q = deque([entrance])
        visited = set()
        visited.add(entrance)
        step = 0
        while q:
            stepLength = len(q)
            for i in range(stepLength): # use length of the deque to iterate through each level
                node = q.popleft()
                # return if exit
                row_boundary = node[0] == 0 or node[0] == len(maze)-1 
                col_boundary = node[1] == 0 or node[1] == len(maze[0])-1
                if (row_boundary or col_boundary) and maze[node[0]][node[1]] == '.' and (node[0],node[1]) != entrance:
                    return step
                for d in dirs:
                    new_node = (node[0]+d[0], node[1]+d[1])
                    if 0<=new_node[0]<len(maze) and 0<=new_node[1]<len(maze[0]):
                        if maze[new_node[0]][new_node[1]] == '.':
                            if new_node not in visited:
                                visited.add(new_node)
                                q.append(new_node)
            step += 1
        return -1

