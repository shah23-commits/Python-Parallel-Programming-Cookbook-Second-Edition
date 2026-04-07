from threading import Thread
import time
import os

# Subclassing the Thread class for a custom implementation
class MyThreadClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       # Subclassing the Thread class for a custom implementation
       print("ID of process running {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    # Creating instances of the custom thread class
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")
  
    # Thread Running (Starting the threads triggers the run() method)
    thread1.start()
    thread2.start()


    # Thread joining (Ensuring the main program waits for these threads to complete)
    thread1.join()
    thread2.join()

    # End 
    print("End")


if __name__ == "__main__":
    main()

    


