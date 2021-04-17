#Example of what you can do with functions

def my_function(x):
    return x * 2

#Print the type of object my_function is
print(type(my_function))

#my function is assigned to variable a
a = my_function

#will return the type of a, which is function
print(type(a))

#will return 20
print(a(10))
