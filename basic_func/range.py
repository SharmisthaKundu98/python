def my_range(*number):
    if len(number) == 1:
        first = 0
        last = number[0]
        step = 1
    elif len(number) == 2:
        first = number[0]
        last = number[1]
        step = 1
    else:
        first = number[0]
        last = number[1]
        step = number[2]
    values = []
    while first != last:
        values.append(first)
        first = first + step
    return values
    

print(my_range(10,1,-1))