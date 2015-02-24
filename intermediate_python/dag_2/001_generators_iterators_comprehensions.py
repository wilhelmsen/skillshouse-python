#!/usr/bin/python
# coding: utf-8

# Iterator.
# Stjålet fra: http://www.shutupandship.com/2012/01/understanding-python-iterables-and.html

# En iterable er:
## En container som har en __iter__ metode.
# En iterator er et objekt som:
## Har en __iter__ metode, som returnerer sig self.
## Har en next metode som returnerer den næste værdi for hvert next-kald.

# En basic iterator.
class MyListIter(object):
    """ A sample implementation of a list iterator. NOTE: This is just a 
    demonstration of concept!!! YOU SHOULD NEVER IMPLEMENT SOMETHING LIKE THIS!
    Even if you have to (for any reason), there are many better ways to 
    implement this."""
    def __init__(self, lst):
        self.lst = lst
        self.i = -1
    def __iter__(self):
        return self
    def next(self):
        if self.i<len(self.lst)-1:
            self.i += 1         
            return self.lst[self.i]
        else:
            raise StopIteration

# Implemennter den.
class MyList(list):
    # initializer ( __init__ ) from list

    # Iter method.
    def __iter__(self):
        return MyListIter(self)

# Brug den.
a = MyList([1, 2, 3, 4])
ia = iter(a)
type(a), type(ia)
for i in a: 
    print i,



# Generators.
def simple_generator():
    yield("Fisk")
    yield("Poelse")
    yield("Torsk")
    yield("Benzinmand")

# Viser at "funktionens" (generatorens) state gemmes for hvert kald.
s = simple_generator()
try:
    print s.next()
    print s.next()
    print s.next()
    print s.next()
    print s.next()
except Exception, e:
    print e

# Vis at call metoden er et generator objekt.
try:
    print s.__call__()
except Exception, e:
    print e

# Brugen af den.
def fib(n):
    a = 0
    b = 1
    counter = 0

    while True:
        if (counter > n): return
        yield a
        a, b = b, a+b
        counter += 1

f=fib(10)
f.next()
f.next()
f.next()

for i in fib(10):
    print i,

print ""

# Generator med en generator i.
def firstn(g, n):
    for i in range(n):
        yield g.next()

print list(firstn(fib(100), 10))


## List comprehensions firkantede paranteser:
l = []
for i in [1,2,3]:
    l.append(i+1)
print l
# Helt basic.
[x for x in [1,2,3]]
# Med operation som eksempel over.
[x+1 for x in [1,2,3]]
# Med condition.
[x+1 for x in [1,2,3] if x%2]
# Dobbel for.
[x+y for x in range(2) for y in range(2)]
# Trippel for med condition.
[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2] 

# Generator Comprehension (runde paranteser)
x = (x **2 for x in range(20))
print(x)
x = list(x)
print(x)

# Set comprehensions:
{x%2 for x in range(20)}
