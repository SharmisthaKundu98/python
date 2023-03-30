def sums(nums):
    nums.append(4)
    return sum(nums)

nums = [1,2,3]
print(nums)
print(sums(nums))
print(nums)

c= [3,4]
a = [1,2,c]
b= a[:]

b[2].append(5)
b.append(6)
print(a)
print(b)