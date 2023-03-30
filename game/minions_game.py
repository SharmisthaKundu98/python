def is_vowel(char):
    return char == "A" or char == "E" or char == "I" or char == "O" or char== "U"
 
def generate_word(s):
    word_list = []
    for i in range(len(s)): #0/1/2/3/4/5 #B/A/N/A/N/A 
        word = s[i]
        word_list.append(word)
        for j in range(i+1,len(s)): 
            word += s[j]
            word_list.append(word)
    return word_list

def minions_game(s):
    stuarts_score = 0
    kelvins_score = 0
    for strings in generate_word(s):
        if is_vowel(strings[0]) == True:
            kelvins_score += 1
        else:  
            stuarts_score += 1
    if stuarts_score > kelvins_score:
        print("Stuart {}".format(stuarts_score))
    elif stuarts_score < kelvins_score:
        print("Kelvin {}".format(kelvins_score))
    else:
        print("Draw")

s = input()
minions_game(s)