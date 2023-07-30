class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # test case:
        # str1 = "ABABAB" str2 = "ABAB" x = "AB"
        # is len(short_str) a divisor of len(long_str)?
        # start with the smaller string and figure out if it indexes the larger one
        # if it does, great
        # if not, remove a character until it does or you're done
        # if long_string.count*len(short) == len(long_String) you found one!
        y = math.gcd(len(str1), len(str2))
        res = str1[:y]
        print(res)
        if res in str2:
            if str1.count(res)*len(res) == len(str1) and str2.count(res)*len(res) == len(str2):
                return res
            else:
                return ""
        else:
            return ""

