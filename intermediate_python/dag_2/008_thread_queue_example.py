#!/usr/bin/python
# coding:utf-8

# når tråde skal snakke sammen

import threading
import time

import Queue

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queue = q

    def print_queue_item(self):
        while not self.queue.empty():
            # lås køen, kaldet blokerere indtil det kommer igennem man kan også
            # sætte den til nonblocking med queueLock.acquire(False)
            # den vil så returnerer False hvis den ikke kan komme igennem til køen
            print(u"{} lås kø".format(self.name))
            queueLock.acquire()
            # tag data
            if not self.queue.empty():
                data = self.queue.get()
                print("{} {}".format(self.name, data))
            # åben køen
            queueLock.release()

            print(u"{} lås kø op".format(self.name))

            time.sleep(1)


    def run(self):
        print "Starting " + self.name
        self.print_queue_item()
        print "Exiting " + self.name



# lav FIFO kø med plads til 100 
workQueue = Queue.Queue(100)

# opret Lås og put nogle værdier i køen
queueLock = threading.Lock()
for i in range(10):
    workQueue.put(i)

# Instantier nye tråde
thread1 = myThread(1, "Thread-1", workQueue)
thread2 = myThread(2, "Thread-2", workQueue)

# Start new Threads
thread1.start()
thread2.start()

# Vent på trådene er færdige
thread1.join()
thread2.join()

print "Exiting Main Thread"


