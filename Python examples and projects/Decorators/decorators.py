#Decorators
#a decorater is a function that takes a function as an input
#and returns another function, the decorated function

#a decorator that doubles 
def double(f):
    #takes parameters of temporary function f as input
    #def g(x,y):
    
    #use these as parameters to account for dynamic arguments
    def g(*args, **kwargs):
        #assigns results of f to variable original_result
        #original_result = f(x,y)
        
        #use these as parameters to account for dynamic arguments
        original_result = f(*args, **kwargs)
        #returns original_result doubled
        return 2 * original_result
    
    #returns the new function
    #function g will replace the function that is passed to
    #function double
    return g

#a decorator that logs
def logging(f):
    def g(x,y):
        print(f"Entering in {f.__name__} with parameters {x} and {y}")
        result = f(x,y)
        print(f"Leaving function {f.__name__} with result {result}")
        return result
    return g

#this will return 40
@double
@double
@logging
def sum(x, y):
    return x + y

@logging
def multiply(a,b):
    return a * b


print(sum(7,3))

print(multiply(5,5))
