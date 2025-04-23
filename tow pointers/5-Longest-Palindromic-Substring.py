class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = 0
        res = ''
        
        def expandAroundCenter(s, left, right):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -=1
                    right +=1
                return s[left+1:right]

        for i in range(len(s)):
            print(i)
            print(s[i])
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)

            if len(len1) > len(len2) and len(len1) > result:
                result = len(len1)
                res = len1
            elif len(len2) > len(len1) and len(len2) > result:
                result = len(len2)
                res = len2
        return res