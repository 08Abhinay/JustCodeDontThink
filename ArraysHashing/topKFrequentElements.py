# import operator

class Solution:
    def topKFrequent(self, nums, k):
        numbers = {}
        
        for number in nums:
            numbers[number] = numbers.get(number, 0) + 1

        # Sort the dictionary items based on values (frequencies) in descending order
        print(numbers.items())
        sorted_elements = sorted(numbers.items(), key=get_frequency, reverse=True)
        # print("sorted_elemets: ",sorted_elements)
        
        # Extract the top k elements
        top_k_elements = []
        for key, _ in sorted_elements[:k]:
            top_k_elements.append(key)
        
        return top_k_elements

def get_frequency(item):
    # print(item)
    return item[1]


# items = [(-1, 2), (1, 1), (2, 2), (3, 1), (4, 1)]

# print("this is the frequency: ",get_frequency(items))

# Example usage:
frequentnumbers = Solution()
k = 2
nums = [4, 1, -1, 2, -1, 2, 3]
result_dict = frequentnumbers.topKFrequent(nums, k)

print(result_dict)



# import operator

# class Solution:
    
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         numbers = {}
        
#         for number in nums:
#             numbers[number] = numbers.get(number, 0) + 1

      
#         sorted_elements = sorted(numbers.items(), key=operator.itemgetter(1), reverse=True)
#         print("sorted_elemets: ",sorted_elements)
        
#         top_k_elements = []
#         for key, _ in sorted_elements[:k]:
#             top_k_elements.append(key)

#         return top_k_elements

       

        
        
