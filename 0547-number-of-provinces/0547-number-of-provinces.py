class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        number_circles = len(isConnected)

        def visit_connected(u: int):
            for v in range(number_circles):
                if isConnected[u][v] == 1 and v not in visited:
                    visited.append(v)
                    visit_connected(v)

        visited = []
        count = 0
        # find an island by iterating through isConnected until we see a '1'
        for i in range(number_circles):
            if i not in visited:
                count +=1
                visited.append(i)
                # mark all connected points as visited by listing them in `visited`
                visit_connected(i)
        return count

        