'''pattern-4
5
    1
   12
  123
 1234
12345
'''
number = int(input())

for i in range(1,number+1):
    print(" "*(number-i),end="")
    for j in range(1,i+1):
        print(j, end="")
    print()    