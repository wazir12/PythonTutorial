Notebook - Classes and Objects
#Classes and objects
class MyRouter(object): #creating a class which inherts from the default "object" class
    def __init__(self, routername, model, serialno, ios): #class constructor; initializing some variables and the method is called whenever you create a new instance of the class
        self.routername = routername #"self" is a reference to the current instance of the class
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)

router1 = MyRouter('R1', '2600', '123456', '12.4') #creating an object by simply calling the class name and entering the arguments required by the __init__ method in between parentheses

router1.model #accessing the object's attributes; result is '2600'

router1.print_router("20150101") #accessing a function (actually called method) from within the class
The router name is:  R1
The router model is:  2600
The serial number of:  123456
The IOS version is:  12.4
The model and date combined:  260020150101

getattr(router2, "ios") #getting the value of an attribute

setattr(router2, "ios", "12.1") #setting the value of an attribute

hasattr(router2, "ios") #checking if an object attribute exists

delattr(router2, "ios") #deleting an attribute

isinstance(router2, MyRouter) #verifying if an object is an instance of a particular class

class MyNewRouter(MyRouter): #creating a new class (child) inheriting from the MyRouter parent class
    ...

issubclass(MyNewRouter, MyRouter) #returns True or False; checking if a class is the child of another class
