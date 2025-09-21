#fiter function

ages=[12,34,45,67,89,45]
def myfun(x):
    return x>39
adults=list(filter(myfun,ages))
print(adults)


#map function
def cube(x):
    return x*x*x
print(cube(3))
numbers=[1,2,3,4,5]
newl=list(map(cube,numbers))
print(newl)

#reduce function
from functools import reduce
def add(x,y):
    return x+y
sum=reduce(add,numbers)
print(sum)