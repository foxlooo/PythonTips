def squareNumbers(nums):
    for i in nums:
        yield (i*i)

my_nums = squareNumbers([1,2,3,4,5])

print(my_nums)
print("First: " + str(next(my_nums)))

for num in my_nums:
    print(num)

print("Another Generator Example: ")
newNumsNotGenerator = [x*x for x in [1,2,3,4,5]]
newNumsGen = (x*x for x in [1,2,3,4,5])
print(newNumsNotGenerator)
print(newNumsGen)
print(list(newNumsGen))

# Infinite Generaor #

def squareInf(num = 10):
    i = 0
    while i != num:
        yield i * i
        i += 1

for x in squareInf():
    print(x)

