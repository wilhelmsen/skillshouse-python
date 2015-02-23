#!/usr/bin/python
# coding: utf-8

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
