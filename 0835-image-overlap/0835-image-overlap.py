class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        # dx, dy represent the translation of img1
        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):

                overlap = 0

                for i in range(n):
                    for j in range(n):

                        # Position in img1 after translation
                        x = i + dx
                        y = j + dy

                        # Check if translated position is inside the matrix
                        if 0 <= x < n and 0 <= y < n:
                            if img1[x][y] == 1 and img2[i][j] == 1:
                                overlap += 1

                ans = max(ans, overlap)

        return ans