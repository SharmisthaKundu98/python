def print_every_nth_num_between_two_numbers(n,first,last):
    number = first
    while number <= last:
        print(number)
        number += n

print_every_nth_num_between_two_numbers(2,1,10)