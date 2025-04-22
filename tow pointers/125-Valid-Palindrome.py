import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        right = len(string) -1
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True