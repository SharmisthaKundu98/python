

def uppercase_1st_letter_all_words_of_a_string(string):     #string = 'i love coding'
        words = string.split()                              #"i","love","coding"
        for n in range(len(words)):                         # n=0,1,2
            letters = words[n]                              # letters = "i"// "love"// "coding"         
            capital = letters[0].upper()                    #letters[0] = "i",capital = "I" // "l","L"//"c","C"
            str = capital + letters[1:]                     #str ="I" // "Love" // "Coding"
            print(str+" ",end="")
        print()                     

uppercase_1st_letter_all_words_of_a_string("i am in love with coding")



