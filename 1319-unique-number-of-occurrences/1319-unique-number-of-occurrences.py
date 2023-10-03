class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = {}
        for i in arr:
            if i in unique:
                unique[i] += 1
            else:
                unique[i] = 1
        print(unique)
        return len(unique.values()) == len(set(unique.values()))

        