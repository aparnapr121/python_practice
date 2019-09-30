"""
1. What is the difference between map, reduce and filter in python
Map function takes a function and an iterable or multiple iterables as parameters.
It apply the function to the iterable and yields an iterator
With multiple iterables, function is applied to all items in paraller. iterator stops when the shortest iterable is exhausted
"""
"""Map"""
l1 = [1, 2, 3, 4]


def square(x):
    return x * x


print("**printing map**")
m1 = map(square, l1)
for x in m1:
    print(x)
l2 = [5, 6]
m2 = map(lambda x, y: x + y, l1, l2)
print("**printing map**")
for x in m2:
    print(x)

"""Filter
filter(function, iterable)
It constructs an iterables for those elements of iterable for which the function returns true
"""
l1 = [1, 2, 3, 4, 5]
f1 = filter(lambda x: x % 2 == 0, l1)
print("**printing filter objects**")
for x in f1:
    print(x)

l2 = [1, 2, 3, 4, 5, [], None, 0]
f1 = filter(lambda x: x, l2)
print("**printing filter objects**")
for x in f1:
    print(x)
"""Wiill not print 0, None, []"""

"""
Reduce moved to functools
Apply a function of two arguments cumulatively to the items of sequence,
from left to right, so as to reduce the sequence to a single value

"""

from functools import reduce

r1 = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print("***printing reduce values***")
print(r1)

"""
2. What is locals
Local namespace
local()
"""

##########################################################################################################################
"""
2
module - single source file
Module is an object of type moducle
Package is a type of module
It can have a module or other packages
A package is a module, the source file that is imported when a package is imported is __init__.py
The package attribute will have a __path__, the path to search to find a module
packages represented by directories
Python checks sys.path attribute for importing module
control imports with __all__
__all__ list of attribute names imported via from module import *

Exceutable directories - specify a main entry point which is run when the package is executed by python

"""
##########################################################################################################################
"""
3
PYTHONPATH - environment variable added to sys.path when python starts
"""
##########################################################################################################################
"""
4.
dir() without arguments returns the list of attributed in the current local scope
with arguments dir(o) returns the a list of valid attributes(methods and variables of the objects 
__dict__ print only the variables
"""


class A:
    def __init__(self):
        self.name = "ClassA"
        self.description = "The description"

    def strlen(self):
        return len(self.name)


a = A()
print("""Printing dir(a)""")
print(dir(a))
print("""Printing dict a""")
print(a.__dict__)
##########################################################################################################################

"""
5. Method resolution order
Ordering of a class's inheritence graph used to define which method is invoked

algorithm for calculating mro - c3
c3 ensures
Subclasses come before base class
base class order from class definition is preserved
First two qualities are preserved no matter where you start in an inheritence graph


"""


class A:
    def func(self):
        return 'A.func'


class B(A):
    def func(self):
        return 'B.func'


class C(A):
    def func(self):
        return 'C.func'


class D(B, C):
    pass


print("""***printing mro""")
print(D.__mro__)
print(D.mro())
d = D()
print(d.func())

"""The following will fail. Since B and C both inherits from A, B and C should come before A in the mro"""
# class D(B,A,C):
#    pass

"""How super works
Given a method resolution order and a class C, super() gives you an object which resolves methods using only the part
of the MRO which comes after C

super(baseclass, derived class) = class bound proxy, claas bound proxy super can only be used to call static/class methods
super() if this is called in an instance method, this is equivalent to super(class of method, self) - instance bound proxy
super() if this is called in an class method, this is equivalent to super(class of method, class) - class bound proxy
python finds MRO for derived-class
it then find the base class in that mro
it takes everything after base class in mro
and finds the first class in that sequence with a matching method name

"""

##########################################################################################################################

"""
6. Property

A decorator which returns a property


"""


class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_farenheit(self):
        return self.temperature * 1.8 + 32


# problems
man = Celsius(10)
print(man.temperature)
man.temperature = 15


# The clients can get and set the attribute object. Inorder to make it private, we can create a property without impacting the client
class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValuError('Temperature less than -273 not possible')
        self._temperature = value

    def to_farenheit(self):
        return self.temperature * 1.8 + 32


##########################################################################################################################
"""
7. What is an iterator
An iterator object must implement two special methods
1. __iter__(), 2. __next__()
This is collectively called the iterator protocol

"""
my_list = [1, 4, 7, 9]

my_iter = iter(my_list)
print("""***printing iterator***""")
print(next(my_iter))

##########################################################################################################################

"""
7. What is a generator

Generators are function that can be paused and resumed on the fly, returning an object that can be iterated ove.
They are lazy
They are memory efficient
Be careful not to mix up the syntax of a list comprehension with a generator expression - [] vs () - since generator expressions can run slower than list comprehensions (unless you run out of memory, of course):
 Keep in mind that generator expressions are drastically faster when the size of your data is larger than the available memory.
 Generators are perfect for reading a large number of large files since they yield out data a single chunk at a time irrespective of the size of the input stream. 
 
 
 Generator function contains one or more yield statement.
When called, it returns an object (iterator) but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.
"""

print("*** Generator section***")


def countdown(num):
    while num > 0:
        yield num
        num -= 1


val = countdown(5)
print(next(val))
print(next(val))

"""
Generators work great for web scraping and crawling recursively:
"""

import requests
import re


def get_pages(link):
    links_to_visit = []
    links_to_visit.append(link)
    while links_to_visit:
        current_link = links_to_visit.pop(0)
        page = requests.get(current_link)
        for url in re.findall('<a href="([^"]+)">', str(page.content)):
            if url[0] == '/':
                url = current_link + url[1:]
            pattern = re.compile('https?')
            if pattern.match(url):
                links_to_visit.append(url)
        yield current_link


"""
Here, we simply fetch a single page at a time and then perform some sort of action on the page when execution occurs.
 What would this look like without a generator? Either the fetching and processing would have to happen \
 within the same function (resulting in highly coupled code that’s hard to test) or we’d have to fetch all the links before processing a single page.
"""

##########################################################################################################################
"""
8. Closures

Closures remember the objects from enclosing scope that the local function needs.
Local function closes over the object it needs preventing it from garbage collected

nonlocal introduces a binding from enclosing name space to local space
"""

print("*** Section for Closure ***")

def outer_func():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func
lf = outer_func()
lf()
print(lf.__closure__)

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
print(square(5))
cube = raise_to(3)
print(cube(5))

##########################################################################################################################
"""
9. What is a decorator

Decorators are a way to enhance or modify the functions without changing their definition

It takes a callable object as argument and returns a callable

"""

def decorator_func(f):
    def local_func(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return local_func

"""
Validation parameter is a use case
A decorator which verifies that the given argument to a function is a non negative number
"""

print(""" Decorator examples """)
def validate(f):
    def wrap(*args, **kwargs):
        if args[1] < 0:
            raise ValueError('Argument must be non negative')
        return f(*args, **kwargs)
    return wrap

@validate
def add(a, b):
    return a + b
print(add(5,4))

"""
We can generalize this and check for argument at any position
"""
def check_non_negative_index(i):

    def validate(f):
        def wrap(*args, **kwargs):
            if args[i] < 0:
                raise ValueError('Argument must be non negative')
            return f(*args, **kwargs)
        return wrap
    return validate

@check_non_negative_index(1)
def add(a, b):
    return a + b
print(add(-5,4))


"""
10. Class method vs static method

Class method is bound to the class, not to the instance
A class method can access or modify class state,
static method can't access or modify class state
static method are grouped inside a class for findability of the function
"""


"""
11. Exception

Exception hierarchy for IndexError
object
BaseException
Exception
LookupError
IndexError


Base Exception
    SystemExit
    KeyboardInterrupt
    GeneratorExit
    Exception
"""

import traceback


print("*** Exceptions ***")
class TriangleError(Exception):
    def __init__(self, message, sides):
        super().__init__(message)
        self.message = message
        self._sides = sides

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return f"{self.message} for sides {self.sides}"

    def __repr__(self):
        return f"Triangle Error here"

def perimeter(a,b,c):
    sides =sorted((a,b,c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    return a+b+c
perimeter(3,4,5)


"""
**kwargs

"""
print("*** usage of kwargs**")
class Employee:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        for key, val  in kwargs.items():
            setattr(self, key, val)

    def __repr__(self):
        return f"{getattr(self,'name')} is {getattr(self, 'height')}"

e = Employee("aparna", 28, place="Whitefield", height="tall")
print(e)


"""
__str__ vs __repr__

these are the protocols to be implemented to call str() and repr()
if __str__() is not implemented, str() will call __repr_().
But if __repr__ is not implmented repr() of super class is invoked
print uses __str__
"""





