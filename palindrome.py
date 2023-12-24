def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    modifiedString = ""
    reveredString = ""

    modifiedString = ''.join(char for char in s if char.isalnum()).lower()
    
    reversedString = modifiedString[::-1]
    print(reversedString)
    return reversedString == modifiedString

print(isPalindrome('Abhinay'))



# def isPalindrome(s):
#     modifiedString = ''.join(char for char in s if char.isalnum()).lower()
#     reversedString = modifiedString[::-1]
    
#     print(reversedString)
#     return modifiedString == reversedString

# print(isPalindrome('Abhinay'))
        