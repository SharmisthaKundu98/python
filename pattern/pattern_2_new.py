'''pattern -2 using data structure

'''
input_1 = int(input())
def making_data_structure(n):
  return range(1,n+1)

def pattern(making_data_structure,char):
  for x in making_data_structure:
    print(char*x)
  

pattern(making_data_structure(input_1),"*")
