camp_cleaning_txt = open(r"C:\Users\kshar\Documents\python\AOC2022\day4\camp_cleaning.txt","r").read()
# camp_cleaning_txt = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
camp_cleaning_txt_data = [[([int(i) for i in string.split("-")]) for string in line.split(",")] for line in camp_cleaning_txt.split("\n")]

assignment_contains = 0

for ((x1,x2),(y1,y2)) in camp_cleaning_txt_data: #7,9 5,7 
    if x1 >= y1 and x2 <= y2:
        assignment_contains += 1
    elif x1 <= y1 and x2 >= y2:
        assignment_contains += 1
    elif x1 == y2 or x2 == y1:
        assignment_contains += 1
    elif x1 <= y1 <= x2 or x1 <= y2 <= x2:
        assignment_contains += 1


print(assignment_contains)