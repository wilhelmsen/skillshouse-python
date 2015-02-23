#!/usr/bin/python
# coding:utf-8

# pip install BeautifulSoup

#
# Husk at køre flask serveren
#

import urllib2
from BeautifulSoup import BeautifulSoup

# hent url og læs data
url = 'http://localhost:5000/hello/keld'
data = urllib2.urlopen(url).read()

# parse data
soup = BeautifulSoup(data)

# undersøg træstruktur
header = soup.contents[3].contents[1]
print header

body = soup.contents[3].contents[1]
print body

# find første element
print soup.find('h1')

# find alle
paragraphs = soup.findAll('p')
for i, p in enumerate(paragraphs):
    print("afsnit {} : {}".format(i, p.string))



