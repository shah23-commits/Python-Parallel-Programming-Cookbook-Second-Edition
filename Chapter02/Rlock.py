import threading
import time
import random


class Box:
    def __init__(self):
        # RLock allows the same thread to acquire the lock multiple times
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        # Nested locking: called by add/remove while they already hold the lock
        with self.lock:
            self.total_items += value

    def add(self):
        # Calls another method that also requests the same lock
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            # Calls another method that also requests the same lock
            self.execute(-1)

def adder(box, items):
    print("N° {} items to ADD \n".format(items))
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("ADDED one item -->{} item to ADD \n".format(items))



def remover(box, items):
    print("N° {} items to REMOVE \n".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("REMOVED one item -->{} item to REMOVE \n".format(items))


def main():
    items = 10
    box = Box()

    t1 = threading.Thread(target=adder, \
                          args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=remover, \
                          args=(box, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
