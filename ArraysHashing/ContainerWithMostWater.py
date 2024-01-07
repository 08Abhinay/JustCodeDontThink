class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxProduct = 0
        
        print(left, right)

        while(left < right):
            if height[left] < height[right]:
                product = height[left] * (right - left)
                left += 1
            else:
                product = height[right] * (right - left)
                right -= 1

            maxProduct = max(maxProduct, product)
        return maxProduct