def sum_of_to_n_even_numbers(n):
    sum = 0
    even = 0
    while even <= n:
        sum = sum + even
        even +=2
    return sum

print("total:",sum_of_to_n_even_numbers(10)) 