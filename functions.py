

print("A simple explaination of functions ")
print()


def greet():
    print("Hi there")
    print("Welcome")


def yellow():
    print("HEllo people")


greet()
print("Explain")
yellow()

print()
print("Defining a function we must set a parameter-- check that out")
print()


def greet(first_name, last_name):
    print(f"Hi {first_name}{last_name}")
    print("Welcome abroad")


greet("Mosh", " F")

print()
print("Some more examples of functions")
print()

# some functions have been defined
# some more functions
print()
print("Vowel counter using functions ")
print()


def vowel_count(s):
    VOWELS = "aeiouAEIOU"
    vc = 0
    for ch in s:
        if ch in VOWELS:
            vc += 1
    return vc


print(vowel_count("GFG is the best platform to learn from."))

print()
print(" A simple program to check whether the given number is odd or even ")
print()


def odd_even(x):

    if (x % 2 == 0):
        print("Even number is given")
    else:
        print("Odd number is given.")


# Driver code for it is
odd_even(4)
odd_even(5)

print()
print("Default Arguments being shown")
print()


def my_Fun(x, y=4):
    print("x: ", x)
    print("y: ", y)


my_Fun(67)

print()
print("*args  ")
print()


def fun(arg1, *argv):
    print("First argument is: ", arg1)
    for arg in argv:
        print("NExt argument is: ", arg)


fun("Hello", "This is life", "Hey there")

print()
print("Keyword arguments")
print()


def myFun(arg1, arg2, arg3, arg4):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    print("arg4:", arg4)


args = ("Geek", "geek2", "geeks3", " ")
myFun(*args)

kwargs = {"arg1": "geek", "arg2": "lejs", "arg3": "jddhj", "arg4": " iu"}
print(kwargs["arg2"])
myFun(**kwargs)

print()
print("Using *args and **kargs in the same line to call the function")
print()


def myFun(*args, **kwargs):
    print("arg1:", args)
    print("arg2:", kwargs)


myFun("Geeks", "for", "geeks", first="GEeks", mid="for", two='KDd')

print()
print("Write a program to create function func1() to accept a variable length of arguments and print their value.")
print()


def func1(*args):
    for i in args:
        print(i)


# call a function with 3 arguments.
func1(20, 40, 60)
print()
# call function with 2 arguments
func1(80, 100)

print()
print("return multiple values from a function")
print()


def calculation(a, b):

    addition = a+b
    subtraction = a-b
    division = a//b
    # return function to return the value
    return addition, subtraction, division


resu = calculation(40, 10)
print(resu)

print()
print("Write a program to create a (DDFAULT FUNCTION) of employee ")
print()


def employee(name, salary=9000):
    print("Name:", name, "Salary:", salary)


employee("Ben", 12200)
employee("Jess")

print()
print("Create an inner function to calculate the addition")
print()


def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5


result = outer_fun(5, 10)
print(result)

print()
print("Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.")
print()


def addition(num):
    if num:
        # recursive functions are those that keep on calling again
        return num+addition(num-1)
    else:
        return 0


add = addition(10)
print(add)

print()
print("Assign a different name to function and call it through the new name")
print()


def display_student(name, age):
    print("name: ", name, "age: ", age)


show_student = display_student
show_student("Emma", 26)

print()
print("Generate a Python list of all the even numbers between 4 to 30.")
print()


print(list(range(4, 30, 2)))


print()
print("The given number is odd or even.")
print()


def odd_even():
    n = 23
    if n != 2:
        print(n, " The number given is even. ")
    else:
        print("The number given is odd ")


odd_even()
