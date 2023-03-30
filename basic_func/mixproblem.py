def sum_of_n(n):
    sum = 0
    for x in range(1,n+1):
        sum += x
    return sum

print(sum_of_n(5))

def product_of_n(n):
    product = 1
    for x in range(1,n+1):
        product *= x
    return product

print(product_of_n(5))

def sum_of_n_in_range(first,last):
    sum = 0
    while first <= last:
        sum += first
        first +=1
    return sum

print(sum_of_n_in_range(3,5))

def product_of_n_in_range(first,last):
    product = 1
    for x in range(first,last+1):
        product *= x
    return product

print(product_of_n_in_range(3,5))

def odd_numbers_in_range(first,last):
    if first % 2 == 0:
        first +=1
    while first <= last:
        print(first,end=" ")
        first +=2

odd_numbers_in_range(1,10)
print()

def even_numbers_in_range(first,last):
    if first % 2 == 1:
        first +=1
    while first <= last:
        print(first ,end=" ")
        first +=2

even_numbers_in_range(1,10)
