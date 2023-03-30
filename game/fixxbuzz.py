
def fizzbuzz(number):
    if number % 3 == 0:
        return "fizzbuzz" if number % 5 == 0 else "fizz"
    return "buzz" if number % 5 == 0 else str(number)

while True:
    number = input()
    if number == "exit":
        break
    string_to_number = int(number)
    print(fizzbuzz(string_to_number))
