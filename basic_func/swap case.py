def swap_case(s):
    '''swap case of the given string
    ShaRmistha --> sHArMISTHA'''
    add_char = ""
    for char in s:
        if char.isupper() == True:
            add_char += char.lower()
        else:
            add_char += char.upper()
    return add_char

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)