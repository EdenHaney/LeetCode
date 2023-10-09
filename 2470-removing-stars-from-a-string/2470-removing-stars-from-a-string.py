class Solution:
    def removeStars(self, s: str) -> str:
        index = s.find('*')
        while index >= 0:
            s = remove_characters(s, index)
            if index > 0:
                index = s.find('*', index-1)
            else:
                index = s.find('*', index)
        return s

    
def remove_characters(s, i):
    # Base case: if index is 0, 
    # return string with first character removed
    if i == 0:
        return s[1:]
    elif i == 1:
        return s[2:]
    return s[0:i-1] + s[i+1:]


        