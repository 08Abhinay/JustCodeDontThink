def product_except_self(nums):
    n = len(nums)
    
    # Initialize left and right arrays
    left_products = [1] * n
    right_products = [1] * n
    
    # Calculate products to the left of each element
    left_product = 1   #[8,2,3,4] 
    for i in range(1, n): #1,2,3
        left_product = left_product * nums[i - 1]   # 0, 1, 2
        # print("left_product: ",left_product)
        
        left_products[i] = left_product
        # print("Into the array:", left_products)
        
    print("final left prod:", left_products)
    
    # Calculate products to the right of each element
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        print("right_product: ",right_product)
        right_products[i] = right_product
        print("Into the array: ",right_products)
    print("final right prod:", right_products)
    
    # Calculate the final result by multiplying left and right products
    result = [left_products[i] * right_products[i] for i in range(n)]
    
    return result

# Example usage:
nums1 = [8, 2, 3, 4]

print(product_except_self(nums1))  # Output: [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
# print(product_except_self(nums2))  # Output: [0, 0, 9, 0, 0]



# class Solution:
#     def productExceptSelf(self, nums):

#         result = []
#         temp = 1
#         for index1, number in enumerate(nums):
#             # print(number)
#             for index2, n  in enumerate(nums):
#                 if index1 == index2 :
#                     continue
#                 temp = temp * n
#             result.append(temp)
            
#             temp = 1
         
#         return result
# solution = Solution()

# print(solution.productExceptSelf([-1,1,0,-3,3]))

    
