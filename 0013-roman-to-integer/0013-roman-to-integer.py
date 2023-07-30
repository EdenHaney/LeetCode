class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        len_s = len(s)
        romans = {"I": 1, "V": 5, "X":10, "L": 50,"C": 100, "D": 500, "M": 1000}
        for i in range(len_s):
            assert s[i] in romans.keys()
            if i < len_s-1:
                if romans.get(s[i+1])/romans.get(s[i]) in [5, 10]:
                    number -= romans.get(s[i])
                else:
                    number += romans.get(s[i])
            else:
                number += romans.get(s[i])
        return number
