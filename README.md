# Interface2.py
A very starting implementation of typescript interfaces in python! I was not satisfied with the dataclasses in python, so I attempted to make something similar to typescript interfaces !! My original plan was to do something like typechat in python, but I realized I needed something better than dataclasses.

The decorators are used to add more functionality to the code. The two current ones are one to make the interface immutable and the other to make it able to take multiple types as a type. I am expecting a TON of bugs, so please lmk if there are any!

To use it, you can clone the repo and then import the IF4 (the main file).

Then, you could do the following:

```
@multiple
class MyInterface(IF4.Interface):
    _properties = {
        "name": str,
        "age": (int, float)
    }
```

You could wrap them with the decorators too! IF you have ANY questions, please leave an issue and ill be happy to get back to you.

This is one of my first public projects! If anyone has any suggestions for changes/improvements/anything please let me know!!
