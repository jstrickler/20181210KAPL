#!/usr/bin/env python

def get_text():
    return "Hello, world"

def shout(text):
    print(text.upper())

t = get_text()
shout(t)

# x = get_text
# print(x)
# print(x())

#  a-z A-Z _ 0-9

x = 5
x = "Bob"
x = 4.3

a = x
x = 6

def rick():
    print("Hello")

x = rick

a = x

x = 5

a()

rick = 5

a()

a = 'something'

def make_string(s: str, size: int=10) -> str:
    return s * size

d = make_string('-', 50)
print(d)

d = make_string('-')
print(d)

def foo(p, *x):
    print(p)
    if x:
        print(x)

foo(5)
foo(5, 6, 7, 8)

x = 5,  # tuple
y = 5   # int

def parse(*, filename, output_folder='/tmp'):
    print(filename, output_folder)

parse(filename="foo.txt", output_folder="/tmp")

parse(filename="bar.txt")
parse(output_folder="DATA", filename='barf')
print()

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

config(animal='wombat', country='Australia', beer="Foster's")



#          POSITIONAL   NAMED
#        required opt  required  opt
def wacky(p1, p2, *p3, p4, p5, **p6):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)

wacky(8, 9, 10, 11, country='Serbia', p5="wombat", animal='platypus', p4=10)

names = ['Ted', 'Susan', 'Wanda', 'Amir']

def add_name(wildebeests):
    wildebeests.append('Brenda')

add_name(names)

print(names)






