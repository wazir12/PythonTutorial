#Try / Except / Else / Finally - handling an exception when it occurs and telling Python to keep executing the rest of the lines of code in the program
try:
    print(4/0) #in the "try" clause you insert the code that you think might generate an exception
    #at some point
except ZeroDivisionError:
    print("Division Error!") #specifying what exception types
    #Python should expect as a consequence of running the code inside the "try" block and how to handle them
else:
    print("No exceptions raised by the try block!") #executed if the code inside the "try" block
    #raises NO exceptions
finally:
    print("I don't care if an exception was raised or not!")
    #executed whether the code inside the "try" block raises an exception or not

#result of the above block
#Division Error!
#I don't care if an exception was raised or not!
