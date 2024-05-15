def caesarCipherEncryptor(string, key):
    # Write your code here.
    length_of_original = len(string)
    end_letter_number = ord(string[-1])
    
    
    
    for number in range(1, key + 1):
        if end_letter_number == 122:
            end_letter_number = 96
        string += chr(end_letter_number + 1)
        end_letter_number = ord(string[-1])
        
    return string[-length_of_original:]



# caesarCipherEncryptor("abc", 26)

print(400%26)

