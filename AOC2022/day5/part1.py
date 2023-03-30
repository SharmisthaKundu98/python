data = open(r"./crate.txt","r").read().split("\n\n")
stack_crates = data[0].split("\n")
crate_data = stack_crates[:-1]

stack = []
for i in range(0,len(stack_crates[-1].split())): #["1","2","3"]
    stack.append([]) #stack = [[],[],[]]

for line in crate_data:
    line_list = [line[i:i+4] for i in range(0,len(line),4)]
    # print(line_list)
    for idx in range(len(line_list)):
        string= line_list[idx]
        if string[0] != " ":
            stack[idx].insert(0,string[1])

procedure = [[int(i.split()[x]) for x in range(1,len(i.split()),2)] for i in data[1].split("\n")]

for (x1,x2,x3) in procedure:
    for i in range(0,x1):
        removed_crate = stack[x2 -1].pop()
        stack[x3 -1].append(removed_crate)
    print(stack)
message = ""
for each in stack:
    message += each[-1]
print(message)
