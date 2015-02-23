#!/usr/bin/python
# coding:utf-8

#
# Multiprocessing er "dyre tråde". Hver "tråd" er en process. Der er for at
# omgå GIL og giver mulighed for at udnytte CPU'en bedre.


# Man kan lave en worker process 
import multiprocessing as mp

class Worker(mp.Process):
    def __init__(self):
        mp.Process.__init__(self)

    def run(self):
        print "Running"
        for i in range(10):
            print i

p = Worker()
p.start()
p.join()


# man kan kører en funktion parallelt med Pool
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':

    # her bliver argumenterne delt ud på 3 af 5 processor 
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))

