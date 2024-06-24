
# my solution by converting into a string. beats 98% of peeps
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        return y==y[::-1]
