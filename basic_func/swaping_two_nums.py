num1= 2
num2= 4

#without_using_another_variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 -num2

'''using a temporary variable
value = num1
num1 = num2
num2 = value'''

'''(num1,num2)=(num2,num1)'''

print(num1,num2)