def total_num_of_even_and_sum(first_num,last_num):
    count = 0
    sum = 0
    if first_num % 2 != 0:
        first_num +=1
    while first_num <= last_num:   
        count +=1
        sum += first_num
        first_num +=2
    
    return count,sum

print(total_num_of_even_and_sum(2,4))
