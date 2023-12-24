class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for letter_s,letter_t in zip(s,t):
            dict1[letter_s] = dict1.get(letter_s, 0) + 1
            dict2[letter_t] = dict2.get(letter_t, 0) + 1
        
        return dict1==dict2

# Create an instance of the Solution class and call the isAnagram method
solution = Solution()
print(solution.isAnagram("anagram", "naaram"))

