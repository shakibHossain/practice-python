# Core Data types :-
# Int - 234, -274

# Float - 27.0, -9.7

# String - "4.6", 'hello'

# Boolean - true-1, false-0

# ----------------------------------

# Output and printing :-
# print("hello", 'end', 87, False) -> always returns string

# ----------------------------------

# Variables :-
# underscore to show spaces, snakecase

# hello = 'test'
# world = 'test2'

# hello_world = 'test3'

# print(hello, world)
# print(hello_world)

# ----------------------------------

# user input :-
# name = input('Type your name: ')
# age = input('Type your age: ')
# print("Your name is", name, "and your age is", age)

# ----------------------------------

# Arithmetic operators :-
x=9
y=3
# x to the power y
result = x ** y 
# Floor division - gives interger result of the division, removes the decimal points
result2 = x // y
# x mod y, returns remainder after division
result3 = x % y

# print(int(x/y))
# print(result2)

# Order of arithmetic operations :-
# B-brackets
# E-exponents
# D-division
# M-multiplication
# A-addition
# S-subtraction

# ----------------------------------

# String methods :-
# hello = 'hello'
# print(hello.upper())
# print(hello.count('ll'))
# x = 'hello'
# y = 'world'

# print(x + y)
# ----------------------------------

# Conditional operators :-
# ==
# !=
# <=
# >=
# <
# >

# and
# or
# not

# precedence - not > and > or

# ----------------------------------

# If/Else/Elif :-
# name = input("Your name: ")

# if name == 'Shakib':
#     print('You are great')
# elif name == "John":
#     print('test')
# else:
#     print('No')

# ----------------------------------

# List/Tuples
# Lists are mutable
# x = [4, True, 'hi']
# y = 'hi'
# print(len(x))
# print(len(y))

# y = x[:] -> Make copy of array x
# y = x
# x[0] = 'hello'
# print(x, y)

# Tuples are immutable
# x = (0,0,2,2)
# x = [[], (), [[], [], [3,4,5]]]

# ----------------------------------

# For loops
# range (start, stop, step)
# by default, only one value in range means it is the stop value
# for i in range(10): 
#     print(i)

# for i in range(-10, -1, 1):
#     print(i)

# x = [3, 4, 42, 3, 2, 4]

# for i in range(len(x)):
#     print(x[i])

# enumerate - will create indexes and values
# for i, element in enumerate(x):
#     print(i, element)

# ----------------------------------

# While loops
# x = [3, 4, 42, 3, 2, 4]

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 10:
#         break

# ----------------------------------

# Slice operator -> works on strings,tuples and lists
# sliced = x[start:stop:step]

# x = [0,1,2,3,4,5,6,7,8]
# s = "hello"
# sliced = x[0:4:2]
# sliced = x[::-1] -> reverse a list
# sliced = s[::-1] -> reverse a string
# sliced = (1,2,3,4,4,2,2,1)[::2]
# print(sliced)

# ----------------------------------

# Sets - unique unordered, unchangeable collection of elements 
# set is one of 4 built-in data types in Python used to store
# collections of data, the other 3 are - Lists, Tuples and Dictionary
# Using a set is very valuable when looking for things, checking for things, removing it compare to list
# x = set()
# s = {4,32,2,2}
# s2 = [3,4, 22,1]
# s2 = {3,4, 22,1}
# s.remove(2) -> removes all instances of 2
# print(s)
# print(4 in s)
# print(4 in s2)
# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))

# ----------------------------------
 
# Dictionary
# it is a key-value pair
# x = {'key' : 4}
# x['key2'] = 8
# del x['key']
# print(x['key'])
# print(list(x.keys()))

# for key, value in x.items():
#     print(key, value)

# ----------------------------------

# Comprehension
# one line initialization of list, tuple, dictionary, etc.
# x = [x % 5 for x in range(5)]
# x = [0 for x in range(5)]
# x = {x for x in range(5)}
# x = tuple(x for x in range(5))
# print(x)

# ----------------------------------

# Functions
# functions are objects so we can return them
# when we return multiple items we get them in a tuple
# optional parameter - by providing an initial value
# def func(x, y, z=3):
    # print('Run', x + y + z)
    # return x, y, z


# print(func(5,6,2))
# r1, r2 = func(5,6)
# print(r1, r2)

# Unpack operator - *args, **kwargs
# Functions are objects so that can be passed around as variables
# def func(x):
#     def func2():
#         print(x)
    
#     return func2

# print(func(3)())
# func(3)()

# def func(*args, **kwargs): -> kwargs - keyword arguments, will allow to pass unlimited amount of regular args and keyword args
#     pass

# x = [1, 23, 2363, 2727]
# print(x)
# print(*x)
# print(**x)

# def func(x, y):
#     print(x, y)

# pairs = [(1,2), (3,4)]

# for pair in pairs:
    # func(*pair)

# func(**{'x': 2, 'y': 5})

# def func(*args, **kwargs):
    # print(*args, kwargs) -> cannot unpack kwargs here

# func(1,2,3,4,5,One=0,Two=1)

# ----------------------------------

# Scope and Global
# x = 'Shakib'

# def func(name):
#     global x
#     x = name

# print(x)
# func('changed')
# print(x)

# ----------------------------------

# Exception
# raise Exception('Bad')
# raise FileExistsError('File not found')

# ----------------------------------

# Handle exceptions
# try:
#     x = 7 / 0
# except Exception as e:
#     print(e)
# finally: -> clean up code, e.g. file close
#     print('finally')

# ----------------------------------

# Lambda - one line anonymous function
# x = lambda x: x + 5
# print(x(2))

# ----------------------------------

# Map and filter

# x = [1,2,3,4,5]

# mp = map(lambda i: i + 2, x) -> map inside elements of x and add 2
# print(list(mp)) -> returns a map, so return as a list

# mp = filter(lambda i: i % 2 == 0, x)
# print(list(mp))

# ----------------------------------

# F Strings - create and manipulate strings
# shakib = 30
# x = f'hello {6 + 8} {shakib}'
# print(x)
