class GroupAnangrams:
    
    def groupAnangrams(self,words):
        
        anagrams = {}
        
        for word in words:
            
            sorted_word = ''.join(sorted(word))
            
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
            
        return list(anagrams.values())
    
grpAnagrams = GroupAnangrams()

input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output_result = grpAnagrams.groupAnangrams(input_strs)
print(output_result)

input_strs = [""]
output_result = grpAnagrams.groupAnangrams(input_strs)
print(output_result)

