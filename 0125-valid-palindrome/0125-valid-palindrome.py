class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()
        while left<right:
            if s[left] == " ":
                left+=1
            if s[right] == " ":
                right-=1
            if s[left].isalpha() or s[left].isdigit():
                if s[right].isalpha() or s[right].isdigit():
                    if s[left] == s[right]:
                        left+=1
                        right-=1
                    else:
                        return False
                else:
                    right-=1
            else:
                left+=1
        return True