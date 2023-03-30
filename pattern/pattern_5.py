'''pattern - 5
5
         1 
       1 2 1
     1 2 3 2 1
   1 2 3 4 3 2 1
 1 2 3 4 5 4 3 2 1
'''
number = int(input())

for i in range(1,number+1):
    print(" "*(number - i)*2,end = " ")
    for j in range(1,i+1):
        print(j,end = " ")
    for k in range(i-1,0,-1):
        print(k,end = " ")
    print()