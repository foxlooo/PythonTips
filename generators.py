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