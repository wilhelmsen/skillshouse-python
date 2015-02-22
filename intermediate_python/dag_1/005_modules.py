#!/usr/bin/python
# coding: utf-8


# Python kommer med batteries included

# importer pakker med os specifikke funktioner
# importer modul
import os

# hvilke filer
print os.listdir('.')

# opret stier
print os.path.join('var','log')

# hvad eksisterer
print os.path.exists('/tmp')

# miljø variable, kan både hentes og sættes
print os.environ['HOME']

# skift mappe
os.chdir(os.environ['HOME'])

print os.listdir('.')

# skift tilbage
os.chdir(os.environ['OLDPWD'])

# importer specific funktion
from os import listdir

listdir('.')

# Det er en dårlig ide at bruge wildcards
from os import *

print environ['HOME']

# import med rename, godt hvis man vil undgå clashes mellem modul navne 
import os as operating_system_module

print operating_system_module.environ['HOME']


#
# øvelse åben en ipython terminal og inspicer os med
#
# import os
# help(os)
#
#
# og os.<tab>
#
# og e.g help(os.listdir)
# 
# Hvad type os sidder du på 
# 
# Mange af os funtionker er møntet på POSIX eller POSIX ligende systemer , se
# hvilke metoder er også virker på windoes her
# https://docs.python.org/2/library/os.html#module-os




