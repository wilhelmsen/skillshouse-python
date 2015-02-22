#!/usr/bin/python
# coding: utf-8


# Python kommer med batteries included

# importer pakker med os specifikke funktioner
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


import sys



