class gfg:

    # The constructor
    def __init__(self, value):
        self._value = value

    # getting the value
    def getter(self):
        print('getting the value')
        return self._value

    # getting the values
    def setter(self, value):
        print("Setting the value  to " + value)
        self._value = value

    # deleting the value
    def deleter(self):
        print("Deleting the statement")
        del self._value

    # create the properties
    value = property(getter, setter, deleter, )


# create a gfg class object
x = gfg("This is the code!")
print(x.value)

x.value = 'Hey this is life'
del x.value
