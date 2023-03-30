import string
rucksack_text = open(r"C:\Users\kshar\Documents\python\AOC2022\day3\rucksack.txt","r").read()
rucksack_text_string = rucksack_text.split("\n")
rucksack_data = [rucksack_text_string[i:i+3] for i in range(0,len(rucksack_text_string),3)]

alphabet_str = string.ascii_lowercase + string.ascii_uppercase
alphabet_list = list(alphabet_str)

total_priorties = 0
for group in rucksack_data:
    for element in group[0]:
         if element in group[1] and element in group[2]:
            total_priorties += (alphabet_list.index(element) + 1)
            break
print(total_priorties)