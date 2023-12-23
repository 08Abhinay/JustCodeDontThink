class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, n in enumerate(nums):
            # Debug point 1: Print the current index and number
            print("Index:", i, "Number:", n)
            
            if n in dict:
                return [dict[n], i]
            else:
                complement = target - n
                dict[complement] = i
                # Debug point 2: Print the dictionary after updating
                print("Dictionary:", dict)

# Test the function with the given input
solution = Solution()
result = solution.twoSum([2, 6, 11, 15,7], 9)
print("Result:", result)
