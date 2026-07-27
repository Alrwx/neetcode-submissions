class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        tmax = 0
        area = 0

        
        while (right - left > 0) :
            area = (right - left) * min(heights[left],heights[right])
            # print(f"{right}, {left} - {area}")
            
            if tmax < area:
                tmax = area
            if heights[left] > heights[right]:
                right = right -1
            else:
                left = left + 1
        return tmax