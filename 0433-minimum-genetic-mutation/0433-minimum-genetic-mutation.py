class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1

        # Define the possible mutations
        options = ['A', 'C', 'G', 'T']

        # Create a queue to store the genes to be checked
        queue = deque()
        queue.append(startGene)

        # Create a set to mark visited genes
        visited = set()
        visited.add(startGene)

        # Counter to keep track of the minimum mutations required to reach end gene
        count = 0
        while queue:
            for i in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return count
                for j in range(len(startGene)):
                    for option in options:
                        newGene = gene[:j] + option + gene[j+1:]
                        if newGene in bankSet and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            count += 1
        return -1