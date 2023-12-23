def check_same_frequencies(my_dict):
    frequencies = list(my_dict.values())
    return len(set(frequencies)) == 1

def wordToDictionary(modifiedWord):
    
    my_dict = {}
    
    # {a:1, b:2}
    for letter in modifiedWord:
        if letter in my_dict:
            my_dict[letter] = my_dict[letter] + 1 
        else:
            my_dict[letter] = 1
    print(my_dict)
    return my_dict      

def equalFrequency(word):
    
    wordList = list(word)
    
    for letter in wordList[:]:
        wordList.remove(letter)
        modifiedWord = wordToDictionary("".join(wordList))
        checker = check_same_frequencies(modifiedWord)
        if checker :
            return True
        else:
            wordList = list(word)
            continue
        
    return False
        
    
print(equalFrequency("aabbcc"))