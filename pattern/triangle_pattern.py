'''
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
'''
def generate_triangle(length): #7
    row = int((length - 1)/2) #
    triangle_list = []
    star_list = [[".|."]*i for i in range(1,row*2,2)] #1,3,5
    for i in range(row): #0/1/2
            each_line = [*["---"]*(row - i),*star_list[i],*["---"]*(row-i)]
            triangle_list.append(each_line)
    mid_list = [*["---"]*(row-1),"-WELCOME-",*["---"]*(row-1)]
    copy_of_triangle_list = triangle_list[0:len(triangle_list)]
    reverse_list = copy_of_triangle_list.reverse()      
    return [*triangle_list, mid_list, *copy_of_triangle_list]

def pattern_printer(data_structure):
    print("\n".join(["".join(row) for row in data_structure]))
    
    
pattern_printer(generate_triangle(11))