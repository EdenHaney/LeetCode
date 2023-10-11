class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cities_dict = defaultdict(list)
        for a,b in connections:
            cities_dict[a].append((b,True))
            cities_dict[b].append((a,False))
        print(cities_dict)
        count = 0
        cities = [0]
        cities_seen = set()
        while(cities):
            node = cities.pop()
            cities_seen.add(node)
            for next_node, pointing_to in cities_dict[node]:
                if next_node not in cities_seen:
                    cities.append(next_node)
                    if pointing_to:
                        count += 1
        return count
                    