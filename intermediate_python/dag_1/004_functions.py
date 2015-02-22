#!/usr/bin/python
# coding: utf-8


# Scoping 
# navne bliver fundet af python i følgene rækkefølge: 
# LEGB rule (Local, Enclosing, Global, Built-in)
# dvs
#   * Det lokale scope f.eks funktion
#   * Hvis der er onkringliggede scopes ... f.eks funktioner
#   * Globalt scope
#   * Indbyggede

# Den indbyggede variable __name__ bliver automatisk sat til navnet på modulet
# her __main__ fordi vi kører modulet som script
print(__name__)

# globalt

__name__ = "GLOBAL"
print(__name__)


def set_and_print_name(name):

    # local scope
    __name__ = name
    print(__name__)

    # inclosing
    def inclosing_name():
        print("inclosing")
        print(__name__)
    inclosing_name()

    # local name er ikke ændret
    print __name__

set_and_print_name('LOCAL')

# Globalt __name__ er ikke ændret
print __name__


# Nu skal vi ændre globale vaiable i en funktion
def set_and_print_name_global(name):
    # her definerer vi at vi bruger den globale variable. Det skal gøres i
    # starten af funktionen
    global __name__
    __name__="local"

print __name__

# nogle scopes bliver hængende

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

# Svar 'local' Det er den global der bliver ændret


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
















