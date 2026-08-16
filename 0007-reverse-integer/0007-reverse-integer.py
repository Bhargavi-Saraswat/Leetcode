class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        result = 0
        while x>0:
            digit = x%10
            x = x//10
            if result > 214748364 or (result == 214748364 and digit>7):
                return 0
            result = (result*10)+digit
        return sign*result