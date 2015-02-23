#!/usr/bin/python
# coding: utf-8


# Scoping
# navne bliver fundet af python i følgene rækkefølge:
# LEGB rule (Local, Enclosing, Global, Built-in)
# dvs
#   * først søges der i det lokale scope f.eks i  funktion.
#   * Hvis der er onkringliggede scopes så søges der i dem.
#   * Ellers søges der i globalt scope.
#   * Tilsidst søges der i det indbyggede scope.

# Den indbyggede variable "__name__" bliver automatisk sat til navnet på modulet
# her __main__ fordi vi kører modulet som script
print(__name__)

# Her sætter vi "__name__" som en global variable i stedet for en builtin
__name__ = "GLOBAL"
print(__name__)


# Her sætter vi __name__ i en funktion
def set_and_print_name():

    # local scope
    __name__ = "local"
    print(__name__)

    # inclosing
    def inclosing_name():
        # __name__ bliver nu fundet i "enclosing scope"
        print("inclosing")
        print(__name__)

    inclosing_name()
set_and_print_name()

# Globalt __name__ er ikke ændret
print __name__




# Nu skal vi ændre globale vaiable i en funktion
def set_and_print_name_global(name):
    # her definerer vi at vi bruger den globale variable. Det skal gøres i
    # starten af funktionen
    global __name__
    __name__ = "local"

print __name__



# I forløkker bliver 
for i in range(100):
    pass

# i findes stadigvæk som det sidste element i range'en
print i


# Øvelse

GLOBAL_VAR = "test"

def change_test():
    GLOBAL_VAR = "enclosing_test"
    def change_enclosing():
        global GLOBAL_VAR
        GLOBAL_VAR = "local"

    change_enclosing()

change_test()

# hvad skal der stå her ?
print GLOBAL_VAR

# SVAR 'local' Det er den global der bliver ændret

# Øvelse hvad sker der med test i enclosing scope skriver den 'local' eller
# 'enclosing'
def change_test():
    test = "local"

    def change_enclosing():
        test = "enclosing"

    change_enclosing()
    print test

change_test()

# I python 2 kan man ikke ændre i parrent scopes som ikke er globale
# I python 3 kan man bruge nonlocal keyword


# Nogle variable er ikke beskyttet så godt af scopes  lists og dicts er
# "mutable" og "inmutable". Vi kan ikke reassigne variable men vi kan godt
# ændre i dem. Også uden 'global'

glist = [0, ]
gdict = {}

def mutable_test():
    glist.append(1)
    gdict['local'] = 0

mutable_test()

print glist
print gdict


# Øvelse hvad sker der her ... virker det

# GLOBAL_VAR = "test"
# def change_test():
#     print GLOBAL_VAR
#     GLOBAL_VAR = "local"
#
# Svar nej ... python fortolkeren bliver forviret man kan ikke mixe globalt og
# local scope.


# Bruger Python lexical eller dynamisk scopes
# see bottom of page comment here : http://stackoverflow.com/questions/6171033/python-noobie-scoping-question

def outer():
    x = "test"
    def inner():
        # Dynamisk scoping for reads
        print x


def outer():
    x = "test"
    def inner():
        # lexical scoping for writes
        x = "inner"

    inner()
    print x != "inner"
    print x == "true"


def outer():
    x = "test"
    def inner():
        print x
        x = "inner"
        # Error !!! can't mix 


#
# Lambda funktioner med mere

# Lambda funtionerner unavngivne funktioner der kan bruges til små filtre. For
# mere komplicerede funktioner er det bedst at bruge en alm. navngivnen
# funktion. En lambda funktion i python kan kun fylde een linje så der er f.eks
# ikke mulighed for if..then..else

l = lambda x: x + 2
l(3) # giver 5

l = lambda x,y: x+y+2
l(3,3)  # giver 8

# lambda funktioner har begrænset funktionalitet de er gode til f.eks maps og reduce

print( map(lambda x: x+3, range(10)))  # lægger 3 til alle tal

print( reduce(lambda x, y: x+y, range(10)))  # lægger alle tal sammen

print( reduce(lambda x, y: x+y, map(lambda x: x*3, range(10))))


#
# nogle functools der måske kan være handy.
# f.eks partials

from functools import partial

# vi fylder det første argument ud på reduce og får en ny funktion der kun
# tager et argument.
my_sum = partial(reduce, lambda x, y: x+y)

print my_sum(range(10))




def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print fib(20)

# Memoization decorator
# Taken from: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
import collections
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

@memoized
def fib(n):
    print "Der kaldes %i"%(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Put evt. timer på også.

# Not cached.
print fib(20)

# Cached.
print fib(20)

