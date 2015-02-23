#!/usr/bin/python
# coding:urf-8

# Django er et større mere integreret framework end Flask. Den kommer med sin
# egen ORM og template engine. Desuden kommer den med en godt backend interface
# hvor man kan oprette og slette database objekter.


# pip install Django


# Django er et MVC framework , Model-View-Controller
#
#  * Model , er ORM'en ... ligesom SQLAlchemy
#  * View, er forretningslogikken ... den der indsatte 'name' i templaten i Flask eksemplet 
#  * Controlleren er url-routingen der sørger for at /hello/lars kommer til den rigtige python metode
#
# I Django er det dog en fil og ikke en dekorator der styrer hvor url'ene peger hen
# Der er også mange der kalder Django for et MVT framework fordi Controller
# delen er så tynd. T'et står så for templates. 

# Django er et mere integreret framework end Flask , Det betyder at hvis man
# har et stor projekt kommer man ofte hurtigere igennem med Django, end med
# Flask. Omvendt er Flask rigtigt godt til simple projekter.
