class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]]= values[i]
            graph[equations[i][1]][equations[i][0]]=1/values[i]
        dec = deque(queries)
        output = []
        while dec:
            query = dec.popleft()
            if query[0] in graph.keys() and query[1] in graph.keys():
                if query[0] == query[1]:
                    output.append(1)
                elif query[1] in graph[query[0]].keys():
                    output.append(graph[query[0]][query[1]])
                else:
                    # recurse graph until we find query[1] from query[0], or run out of places to go                
                    go_next = deque(graph[query[0]])
                    while go_next:
                        next_vertex = go_next.popleft()
                        for value in graph[next_vertex]:
                            if value != query[0] and value not in graph[query[0]].keys():
                                graph[query[0]][value] = graph[query[0]][next_vertex]*graph[next_vertex][value]
                                go_next.append(value)
                    if query[1] in graph[query[0]].keys():
                        output.append(graph[query[0]][query[1]])
                    else: 
                        output.append(-1)
            else:
                output.append(-1)
        print(graph)
        return output