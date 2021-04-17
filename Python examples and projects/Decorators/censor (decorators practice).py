#Decorators continued
#a decorater is a function that takes a function as an input
#and returns another function, the decorated function


#Decorator censor- takes a function as an input and creates a new function with
#with the same arguments as function "f"

#define a set
#note that we have not defined a list
#we do this because for time complexity reasons: if we search
#FORBIDDEN_WORDS for an item, the complexity will be O(1) (on average)
#as opposed to the O(n) time complexity of a list
FORBIDDEN_WORDS = {"javascript","java"}


#we are decorating function f
def censor(f):
    #passing generic arguments
    #function g should behave exactly like function f, but then
    #examine the output of function f and replace forbidden words with
    #something else
    def g(*args, **kwargs):
        #first, we must call the original function
        originalResult = f(*args, **kwargs)

        #split this originalResult string into words
        listOfWords = originalResult.split(" ")
        #for every word in the listOfWords, I will append the words
        #that are not forbidden to the output list
        outList = []

        for eachWord in listOfWords:
            if eachWord.lower() in FORBIDDEN_WORDS: #O(1) in average
                #appends asterisks in place of forbidden word found
                outList.append("*" * len(eachWord))
            else:
                outList.append(eachWord)
                
        return " ".join(outList)
    
    #return the new function
    return g

@censor
def myFunction():
    a = input("Type a sentence: ")
    return a

print(myFunction())
            
        
        
