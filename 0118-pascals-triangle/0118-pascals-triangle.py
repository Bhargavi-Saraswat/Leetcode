class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        a = []
        for i in range(numRows):
            a = []
            for j in range(i+1):
                if j == 0 or j == i:
                    a.append(1)
                else:
                    v = ans[i-1][j-1]+ans[i-1][j]
                    a.append(v)
            ans.append(a)
        return ans