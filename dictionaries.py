#dictionary is unordered set of key value pairs separated by , and enclosed in {};Mutable;
dict = {} # empty dictionary
print("dictionary:%s"%dict)
print("Type of Dict: %s"%type(dict))    #output: <class,'dict'>
dict={"Vendor":"apple","OS":"Mac","Model":"MacbookAir"} #dict
print(dict)
#keys in dictionary must be unique and have a immutable type like String.However, Values can be immutable
#Accessing dictionary elemensts:
print("OS:%s "%dict["OS"])
#Adding element in dictionary
dict["RAM"]="16GB"
print("Dict:%s "%dict)
#updating values in dictionary
dict["OS"] = "IOS"
print(dict)
del dict1["Ports"]  #deleting a key-value pair from the dictionary

len(dict1) #returns the number of key-value pairs in the dictionary

"IOS" in dict1 #verifies if "IOS" is a key in the dictionary

"IOS2" not in dict1 #verifies if "IOS2" is not a key in the dictionary

#Dictionaries - methods
dict1.keys() #returns a list having the keys in the dictionary as elements

dict1.values() #returns a list having the values in the dictionary as elements

dict1.items() #returns a list of tuples, each tuple containing the key and value of each dictionary pair

#Conversions between data types
str() #converting to a string
int() #converting to an integer
float() #converting to a float
list() #converting to a list
tuple() #converting to a tuple
set() #converting to a set
bin() #converting to a binary representation
hex() #converting to a hexadecimal representation
int(variable, 2) #converting from binary back to decimal
int(variable, 16) #converting from hexadecimal back to decimal
