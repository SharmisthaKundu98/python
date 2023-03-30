
full_data = open(r"C:\Users\kshar\Documents\python\AOC2022\day7\dirSize.txt","r").read().split("\n")
# data = full_data[2:]
# dir_file_full_data = [string.split() for string in data]

# sub_dir = {}
# dir_size = {}

# def cal_size(dir):
#     direc_size = dir_size[int(x1)]
#     for i in sub_dir[x1]:
#         if i in sub_dir:
#             direc_size +=  cal_size(i)
#     return direc_size

# for line in full_data:
#     if line[0] == "$":
#         cmd_line = line.split()
#         print(cmd_line)
#         if cmd_line[1] == "cd":
#             path = cmd_line[2]
#             if path == "/":
#                 curnt_dir = path
#             else:
#                 curnt_dir = path + cmd_line[2]
#             if curnt_dir not in sub_dir:
#                 sub_dir[curnt_dir] = []
#                 dir_size[curnt_dir] = 0
#     else:
#         x1,x2 = line.split()
#         if x1 == "dir":
#             sub_dir[curnt_dir].append(x2)
#         else:
#             dir_size[curnt_dir] += int(x1)
#         # print(dir_size)



# print(cal_size("a"))

# # print(full_data)

