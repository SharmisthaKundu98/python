calories_data_file = open("C:/Users/kshar/Documents/python/AOC2022/day1/calories.txt","r")
calories_data = calories_data_file.read()
elf_calories_data = calories_data.split("\n\n")
# list_elf_callories = []
# for elf in elf_calories_data:
#     list_elf_callories.append(elf.split("\n"))

list_elf_callories = [elf.split("\n") for elf in elf_calories_data]
print(list_elf_callories)

total_calories_elf = [[sum(elf[i]) for i in range(len(elf))] for elf in list_elf_callories]
# for elf in list_elf_callories:
#     sum_cal = 0
#     for i in range(len(elf)):
#         sum_cal += int(elf[i])
#         total_calories_elf.append(sum_cal)
#sum_calories_of_1st_elf_carring_most_calories-----part_1
print(max(total_calories_elf))

#total_calories_of_1st_three_elf_carring_most_calories------part_2
print(sum(sorted(total_calories_elf)[-3:]))

#print(max([sum(elf) for elf in [ [int(cal) for cal in elf_str.split("\n") ]   for elf_str in calories_data.split("\n\n")]]))