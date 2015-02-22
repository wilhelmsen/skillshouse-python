#!/usr/bin/env python
# coding: utf-8

[1,2,3,4]
liste = ["hest", 1, True, 200+1]
liste.append("John Rambo")
print liste
print liste[0]
print len(liste)
print liste[-1]
print "Slice"
print liste[2:-2] # slices.

# Key value (dict)
dictionary = {"a": 1, "23+1": 14 }
dictionary['fisk'] = "torsk"
print dictionary
print dictionary.keys()
print dictionary.values()

for key, value in dictionary.iteritems():
    print key, value

if "fisk" in dictionary:
    print dictionary["fisk"]
else:
    print "Fisk er ikke i dictionary..."


# Tuples
t = (1,2,3,4,4,5,6,)
print t
try:
    t[0] = 100
except TypeError, e:
    # man kan ikke ændre en tuple
    pass

# Ordnet set
s1 = set([1,6,2,3,4,4,4,4,4,4,1,2,2,6,5,7,4,6,5,7,8])    
print(s1)

# test om 8 er i sættet
print 8 in s1

s2 = set([1,2,100])

# fællesmængde
print s1.union(s2)


# String

str1 = "hello"

# strenge virker som lists
for i in str1:
    # skriver hvert element ud
    print i

# string concat
print str1 + str1

# string search 
print "he" in str1


# string replace
print str1.replace("he", "she")

# to string
print str(1)
print "%s %d %.2f" % (1.123, 1.223, 1.123)
print "To {be} or not to {be}".format(be="bee")

