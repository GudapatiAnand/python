import threading
from threading import *
from time import sleep

class first_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"This is 1st Thread")
            sleep(1)

class second_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"This is 2nd Thread")
            sleep(1)

t1=first_thread()
t2=second_thread()
t1.start()
print(t1.is_alive())
t2.start()
print(t1.is_alive())
t1.join()
t2.join()
print(t1.is_alive())
print(t2.is_alive())

# import threading
# print(threading.current_thread().getName())