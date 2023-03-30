def collatz_function(number):
    collatz_list = [number]
    next = number
    while next > 1:
        if next % 2 == 0:
            next = next/2
        else:
            next = 3*next + 1
        collatz_list.append(next)

    return collatz_list

print(collatz_function(5))
        
        