class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i-stack[-1]-1
                else:
                    width = i
                area = max(area,height*width)
            stack.append(i)
        return area