# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high = n
        low = 1
        num_to_guess = n
        guess_result = guess(num_to_guess)
        while guess_result != 0:
            if guess_result == -1:
                high = num_to_guess
                num_to_guess = int(high - (high-low)/2)
            elif guess_result == 1:
                low = num_to_guess
                num_to_guess = int(low + (high-low)/2)
            guess_result = guess(num_to_guess)

        return num_to_guess
        

        