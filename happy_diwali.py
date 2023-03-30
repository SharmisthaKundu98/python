from distutils.command.build_scripts import first_line_re
import  math

def HAPPY_DIWALI(line):
    print(line)
    pattern_printer(pattern_h(5),"*")
    print()
    pattern_printer(pattern_a(5),"*")
    print()
    pattern_printer(pattern_p(5),"*")
    print()
    pattern_printer(pattern_p(5),"*")
    print()
    pattern_printer(pattern_y(5),"*")
    print()
    pattern_printer(pattern_d(5),"*")
    print()
    pattern_printer(pattern_i(5),"*")
    print()
    pattern_printer(pattern_w(5),"*")
    print()
    pattern_printer(pattern_a(5),"*")
    print()
    pattern_printer(pattern_l(5),"*")
    print()
    pattern_printer(pattern_i(5),"*")
    
def pattern_h(length):
    return [
        [True,*[False]*(length-2),True] if i != math.ceil(length/2) else [True]*(length) for i in range(1,length+1)
    ]

def pattern_a(length):
    return [
        [True,*[False]*(length-2),True] if i != 1 and i != math.ceil(length/2) else [True]*(length) for i in range(1,length+1)
    ]

def pattern_p(length):
    first_mid_line = [True if i%2 != 0 else False for i in range(1,length+1)]
    upto_mid_line = [True if i == 1 or i == length else False for i in range(1,length+1)]
    upto_mid_list = [
        first_mid_line if i == 1 or i == (math.ceil(length/2)) else upto_mid_line for i in range(1,(math.ceil(length/2))+1)
    ]
    return [
        *upto_mid_list,*[[True] for i in range(length - math.ceil(length/2))]
    ]

def pattern_y(length):
    upto_mid_line = [True if i == 1 or i == length else False for i in range(1,length+1)]
    mid_line = [True if i%2 != 0 else False for i in range(1,length+1)]
    upto_mid_list = [
        mid_line if i == (math.ceil(length/2)) else upto_mid_line for i in range(1,(math.ceil(length/2))+1)
    ]
    remaining_list =[True if i == (math.ceil(length/2)) else False for i in range(1,length+1)]
    return[
        *upto_mid_list, *[remaining_list for i in range(length -math.ceil(length/2))]
    ]

def pattern_d(length):
    first_last_row = [*[True]*math.ceil(length/2),*[False]*(length- math.ceil(length/2))]
    mid_row = [True if i == 1 or i == length else False for i in range(1,length+1)]
    
    return [
        first_last_row,*[mid_row for i in range(2,length)],first_last_row
    ]

def pattern_i(length):
    mid_row = [True if i == math.ceil(length/2) else False for i in range(1,length+1)]
    return [
        [True]*length,*[mid_row for _ in range(2,length)],[True]*length 
    ]

def pattern_w(length):
    upto_mid_row = [True if i == 1 or i == length else False for i in range(1,length+1)]
    mid_row = [True if i == 1 or i == length or i== math.ceil(length/2) else False for i in range(1,length+1)]
    remaining_row = [True if i != math.ceil(length/2) else False for i in range(1,length+1)]
    return [
        *[upto_mid_row for _ in range(1,math.ceil(length/2))],
        mid_row,
        *[remaining_row for _ in range(1,length - math.ceil(length/2))],
        upto_mid_row
    ]

def pattern_l(length):
    return [
        *[[True] for _ in range(1,length-1)],
        [True if i == 1 or i == length else False for i in range(1,length+1)],
        [True]*length 
    ]


def pattern_printer(data_structure,char):
    for row in data_structure:
        for position in row:
            print(char if position else " ",end = "")
        print()


HAPPY_DIWALI(" BEST WISHES FOR YOU FROM SHARMISTHA :")