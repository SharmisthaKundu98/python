def nth_fibbonacci(number):
    if number  > 0:
        print(0)
    if number > 1:
        print(1)
    number_1 = 0
    number_2 = 1
    count = 3
    while count <= number:
        number_3 = number_1 + number_2
        number_1 = number_2
        number_2 = number_3
        count += 1
        print(number_3)

nth_fibbonacci(4)