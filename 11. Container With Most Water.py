class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i != j:
            if height[i] < height[j]:
                max_area = max(max_area, (height[i] * (j - i)))
                i += 1
            else:
                max_area = max(max_area, (height[j] * (j - i)))
                j -=1
        return max_area

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))