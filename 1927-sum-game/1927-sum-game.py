class Solution:
    def sumGame(self, num: str) -> bool:
        left = 0
        right = 0
        mid = len(num)//2
        d = 0
        for i in range(mid):
            if num[i] == '?':
                left += 1
            else:
                d += int(num[i])
        for i in range(mid,len(num)):
            if num[i] == '?':
                right += 1
            else:
                d -= int(num[i])
        return 2*d != 9*(right-left)