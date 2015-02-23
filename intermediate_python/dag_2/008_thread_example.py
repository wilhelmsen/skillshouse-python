#!/usr/bin/python
# coding:utf-8

# Et simplet tråd eksempel
# bemærk at tråde ikke giver bedre udnyttelser af CPU på grund ad pythons GIL (Global Intepreter Lock) 
# så Python fortolkeren kan kun kører en tråd ad gangen. Det er fordi pythons
# memory management ikke er trådsikkert se
# https://wiki.python.org/moin/GlobalInterpreterLock



# tråde nedarver fra threading modulet
# en tråd starter ved at man kalder dens run metode

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def print_time(self, counter, delay):
        while counter:
            time.sleep(delay)
            print "%s: %s" % (self.name, time.ctime(time.time()))
            counter -= 1

    def run(self):
        print "Starting " + self.name
        self.print_time(self.counter, 1)
        print "Exiting " + self.name


# Create new threads
thread1 = myThread(1, "Thread-1", 5)
thread2 = myThread(2, "Thread-2", 5)

# Start new Threads
thread1.start()
thread2.start()

# Vent på trådene er færdige
thread1.join()
thread2.join()

print "Exiting Main Thread"


