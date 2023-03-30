data = open(r"C:\Users\kshar\Documents\python\AOC2022\day6\marker.txt","r").read()

for i in range(0,len(data)):
    position = i + 4
    if len(set(data[i:i+4])) == 4:
        break
first_maker = position
# print(data)
print(first_maker)