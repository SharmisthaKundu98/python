import string
rucksack_text = open(r"C:\Users\kshar\Documents\python\AOC2022\day3\rucksack.txt","r").read()
rucksack_text_string = rucksack_text.split("\n")
rucksack_data = [[compartments[:int(len(compartments)/2)],compartments[int(len(compartments)/2):]] for compartments in [list(rucksack) for rucksack in rucksack_text_string]]

alphabet_str = string.ascii_lowercase + string.ascii_uppercase
alphabet_list = list(alphabet_str)

total_priorties = 0
for rucksack in rucksack_data:
    for element in rucksack[0]:
         if element in rucksack[1]:
            total_priorties += (alphabet_list.index(element) + 1)
            break
print(total_priorties)