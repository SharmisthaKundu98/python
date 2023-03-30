'''pattern using data structure
'''
def generate_pattern_1(length):
    '''
    * * * * * 
    *       *
    *       *
    *       * 
    * * * * *
    '''
    first_last_row = [True]*length
    mid_space = [False]*(length-2) #[False,False,False]
    return [
        first_last_row,
        *[[True,*mid_space,True] for _ in range(length-2)],
        first_last_row
    ]                           #[True,False,False,False,True] 

def generate_pattern_2(length):
    '''
    5         4           3
    * * *     * * * *     * * *
     * *      * * * *      * *
    * * *     * * * *     * * *
     * *      * * * *
    * * * 
    '''
    row = [True if i%2 != 0 else False for i in range(1,(length**2)+1)]
    return [row[i:length+i] for i in range(0,len(row),length)]

def generate_pattern_3(length):
    '''
     5
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    '''
    increasing_row= [[True]*i for i in range(1,length+1)]
    decreasing_row = [[True]*i for i in range(length-1,0,-1)]
    return [*increasing_row,*decreasing_row]

'''
5
    *
   ***
  *****
 *******
*********
'''
def generate_triangle(length):
    triangle_list = []
    star_list = [[True]*i for i in range(1,length*2,2)] #1,3,5,7,9
    for i in range(1,length+1): #1/2/3/4/5
            each_line = [*[False]*(length-i),*star_list[i-1]]
            triangle_list.append(each_line)
    return triangle_list
    
def pattern_printer(data_structure, char):
    for row in data_structure:
        for position in row:
            print(char if position else " ",end= "")
        print()

pattern_printer(generate_pattern_3(int(input())),"*")