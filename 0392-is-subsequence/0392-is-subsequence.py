class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        count = 0
        for char in s:
            for j in range(index,len(t)):
                print(t[j])
                if char == t[j]:
                    index = j + 1
                    count +=1 
                    print(index)
                    break
            print(char)
        return count == len(s)
s = Solution()
s.isSubsequence("ab", "baab")