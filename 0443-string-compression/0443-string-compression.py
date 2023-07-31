class Solution:
    def compress(self, chars: List[str]) -> int:
        result = 0
        index = 0
        while index < len(chars):
            count = 1
            while index + count < len(chars) and chars[index + count] == chars[index]:
                count += 1
            chars[result] = chars[index]
            index += count
            result += 1
            if count > 1:
                for c in str(count):
                    chars[result] = c
                    result += 1
        return result