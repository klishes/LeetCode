class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string into a list of words
        words = s.split()

        # get the last word
        last = words[-1]
        count = len(last)
        # return the length of the last word
        return count