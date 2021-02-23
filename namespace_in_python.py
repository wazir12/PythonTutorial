
#https://www.python-course.eu/python3_namespaces.php
#Namespaces in Python are implemented as Python dictionaries,that is, they are defined by a mapping of names,
#i.e. the keys of the dictionary, to objects, i.e. the values.
#The user doesn't have to know this to write a Python program and when using namespaces.
#Some namespaces in Python:

#global names of a module
#local names in a function or method invocation
#built-in names: this namespace contains built-in fuctions (e.g. abs(), cmp(), ...) and
#built-in exception names

#Lifetime of a Namespace
#The namespace containing the built-in names is created when the Python interpreter starts up,
#and is never deleted.
#The global namespace of a module is generated when the module is read in.
#Module namespaces normally last until the script ends, i.e. the interpreter quits.
# When a function is called, a local namespace is created for this function.
#This namespace is deleted either if the function ends, i.e. returns, or if the function raises an exception,
#which is not dealt with within the function.

#Modules and importing - Basics
import sys #importing the sys module; the import statements should be placed before any other code in your application

from math import pi #importing only a variable (pi) from the math module

from math import sin #importing only a function (sin()) from the math module; there's no need to add the parantheses of the function when importing it

from math import * #importing all the names (variables and functions) from the math module
