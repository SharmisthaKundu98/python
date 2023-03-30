def factorial_of_a_number(number):
    fact = 1
    while number >= 1:
        fact = fact * number
        number -=1
    return fact

print(factorial_of_a_number(5))
print(__name__)