"""def multiplication_table(m,n):
    for count in range(1,n+1):
        print("%d x %d = %d"%(m,count,m*count))

multiplication_table(10,5)"""

def multiplication_table(m,n):
    table = [m*count for count in range(1,n+1)]
    return table   

print(multiplication_table(10,5))