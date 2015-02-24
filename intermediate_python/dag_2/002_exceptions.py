#!/usr/bin/python
# coding: utf-8

# Exceptions: Til fejlhåndtering. Exception. Noget der ikke sker så ofte.

# IOError er speciel
import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:
    print "No valid integer in line."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise


# To i samme:
except (IOError, ValueError):


# Finally.
# Kører uaset hvad.

# Egen. Simpel.
class E(Excepion):
    pass

# Else.
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print 'cannot open', file_name
else:
    text = fh.readlines()
    fh.close()

if text:
    print text[100]

# Assert.
#assert()

# is instanceof(list) eller str, fx.
