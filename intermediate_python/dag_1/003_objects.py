#!/usr/bin/env python
# coding: utf-8

# Functions
# Hello world.
def print_hello_world():
    """
    En docstring 
    prints hello world 
    """
    print "Hello verden"

print_hello_world()

# docstrings er altid en god ide. ..virker med help(print_hello_world)
print print_hello_world.__doc__


# Default værdier.
def print_hej(navn="Dårde"):
    print "Hej %s! Håber du har det godt?"%(navn)

print_hej()
print_hej("John Rambo")
print_hej(232)

def add(a, b=2, c=3):
    return a + b + c

print add(1,1)
print add(1)
print add(1, c=23)

# argumenter er bare en tuple og en dict

def new_add(*args, **kwargs):
    return args[0] + kwargs['b'] + kwargs['c']

print new_add(1, b=15, c=23, d=15)

# Man kan bygge argumenterne op fra en dict.
mine_kw_argumenter = {'b' : 15, 'c' : 23, 'd': 15}
mine_args = (1,2,3)
print new_add(*mine_args, **mine_kw_argumenter)


# Man kan returnere flere værdier.
def returner_flere_values():
    return 1,2,3,4

var1, var2, var3, var4 = returner_flere_values()
print var1, var2, var4


# Python functioner er objekter, som kan assignes til variable
# De eksekveres igennem at bruge ()-operatoren (__call__-opretaoren)
mit_navn = print_hej
mit_navn("John Rambo")

# Man kan give en funktion som argument til en funktion.
def print_mit_navn(f, navn):
    f(navn)

print_mit_navn(mit_navn, "John Rambo")


# Class
class A:
    pass

class B:
    # Initializer
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Nedarvning.
class C(B):
    def __str__(self):
        return "C: %s %s"%(self.a, self.b)

b = B(1, 2)
print b
c = C(1, 2)
print c

# Instance attributes.
print b.__dict__
print c.__dict__


# Class variables.
class D:
    # Class variable.
    i = 1

class E(D):
    pass

# Instance variable.

# __dict__
d = D()
e = E()
print d.__dict__
print D.__dict__
print E.__dict__
print e.__dict__

d1.i = 100
print d.__dict__
print D.__dict__
print E.__dict__
print e.__dict__

# Attribute:


# property
class F:
    pass



##
# Metode:
##
class G:
    def __init__(self):
        self.a = 2

    def add(self, value):
        return self.a + value

g = G()
print g.add(25)



# Polymorphism
class H():
    def myname(self):
        print "H"
class I(H):
    def myname(self):
        print "I"
class J(H):
    def myname(self):
        print "J"

names_list = [H(), I(), J()]

for i in names_list:
    if isinstance(i,H):
        print i.myname()
    
    print i.myname()

#isinstance








# Duck typing.
# Fra wikipedia.
#http://en.wikipedia.org/wiki/Duck_typing#In_Python
class Duck:
    def quack(self):
        print "Quack, quack!"
    def fly(self):
        print "Flap, Flap!"
 
class Person:
    def quack(self):
        print "I'm Quackin'!"
    def fly(self):
        print "I'm Flyin'!"
 
def in_the_forest(mallard):
    mallard.quack()
    mallard.fly()
 
in_the_forest(Duck())
in_the_forest(Person())




# Decorator:
# From https://www.andreas-jung.com/contents/a-python-decorator-for-measuring-the-execution-time-of-methods
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

class Foo(object):

    @timeit
    def foo(self, a=2, b=3):
        time.sleep(0.2)

@timeit
def f1():
    time.sleep(1)
    print 'f1'

@timeit
def f2(a):
    time.sleep(2)
    print 'f2',a

@timeit
def f3(a, *args, **kw):
    time.sleep(0.3)
    print 'f3', args, kw

f1()
f2(42)
f3(42, 43, foo=2)
Foo().foo()
