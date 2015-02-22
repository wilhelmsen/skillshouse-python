#!/usr/bin/env python
# coding: utf-8

# Variabelnavne og funktionsnavne SKAL starte med et bogstav, "_", dvs. bogstaver, som ikke kan forvæksles med en operator.
# Fx:
a = 1
a_123 = "fisk"
n = None
t = True
f = False
# 123_a = "FAILS" # Må ikke starte med et tal.

# Epressions:
# Må alle de normale operatorer, fx +, -, *, 
1+2
2-1
"fisk" + "pølse"
a*12

# Indentering!! 4 spaces (pep8).
try: 
    "a"+2
except TypeError, e:
    print e

t and f
f or t

t is True
t is not False

# Try/raise/except/except
try:
    raise RuntimeError("Av")
except RuntimeError, e:
    pass
except Exception, e:
    print(e)

# is og is not , sammenligner på instans niveau mens == og =! sammenligner værdier
# Python har kun een None instans derfor kan man sammenligne på instans niveau

# i udtryk med 'or' eller 'and' bliver udtrykkede evalueret fra venstre dvs i 
True or (2 != 3)
# bliver 2 != 2 ikke evalueret
False and (2 != 3)
# her bliver det sidste udtryk heller ikke evalueret


# Simple statements
# E.g.:
# Assignments:
a = 1 + 2
b = a + 23

# if, elif, else
if a == 1:
    print("A er 1")
elif a == 2 or a ==3:
    print("A er 2 eller 3")
elif a is not None and a==4:
    print("A er ikke None og er 4")
else:
    print a

# for, while
# For.
for i in [1,2,3,4,5]:
    if i == 4:
        # TODO: handle i == 4
        pass # Null operator. Laver intet.
    elif i == 1:
        continue # Op igen til for, hvor i = 2
    if i == 3:
        break # 
    print i

# While.
i = 0
while True:
    i += 1
    if i > 5:
        break

# switch/case skal laves med if/else.
