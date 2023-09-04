# next, we will learn how to use the decorators I defined 

#    note: PLEASE GIVE IDEAS FOR MORE!

# first, imports
import IF4

# the decorators are in the decorators folder
# right now, the three are:
#       1. A decorator to make the interface immutable
#       2. A decorator to make the interace accept multiple types as the type declaration
#       3. A decorator to allow default values in the declaration

# for the first example, we will use the  immutable decorator

from decorators.immutableIF4 import immutable

# to use it, simply wrap the Interface you want to apply in it

@immutable
class Example(IF4.Interface):
    _properties = {
        "name": str
    }

# to demonstrate, create an example object

ex = Example(name="Asher")

# if we try to find the name associated with it:

ex.name     # returns "Asher"


#now, if we try to change it:

ex.name = "Sam"

# we will get the error: '''AttributeError: Cannot modify immutable property name'''

# -------------------------------------------------- #

# now, we will demonstrate the multiple decorator

# imports

from decorators.multipleIF4 import multiple

# to use it, follow the following example:

@multiple
class MultExample(IF4.Interface):
    _properties = {
        "name": (str, bool)
    }

# as you can see, we define the types in a tuple, and then it will accept either of those types

# for example:

ex = MultExample(name=True)      #allows it

ex.name         # returns True

ex.name = "Hi"     #also allows it

ex.name    #returns "Hi"



# ---------------------------------------------------------#


# lastly, we will use the default  value decorator

# imports

from decorators.defaultIF4 import defaultval

# this time, similarly to multiple, we will wrap it in the defaultval and then use a tuple as a type, 
# with the second value being the default val

# for example:

class DefExample(IF4.Interface):
    _properties = {
        "name": (str, "Anon")
    }


# if we inialize an object without any input:

ex = DefExample()

# and we check the name

ex.name     # it returns the default value!

# and, it allows us to inialize an object with a value 

