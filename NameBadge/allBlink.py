from sense_hat import SenseHat
from time import sleep
from random import randint
import random
import threading
import time
#import timeit

import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

exitFlag = 0



class blinkThread (threading.Thread):
    nbrPixelChanges = 0
    durationMultiples = [2,3,5,7,11,13,17,19,23,29,31,41,43,47]
    #durationMultiples = [10]

    def __init__(self, threadID, name, counter, sense, x, y):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.sense = sense
        self.x = x
        self.y = y
        self.startTime = time.time()
        self.endTime = time.time()
        self.durationMultiple = random.choice(blinkThread.durationMultiples)
    def run(self):
        #print('\n' + "Starting " + self.name)
        counter = 0
        while counter in range(100):
            
            x = self.x
            y = self.y
            rval = randint(0,255)
            gval = randint(0,255)
            bval = randint(0,255)
            self.sense.set_pixel(x,y,rval,gval,bval)
            blinkThread.nbrPixelChanges += 1
            randval = round(self.durationMultiple * random.random(), 1)
            #print(str(blinkThread.nbrPixelChanges) + " -> set pixel x:" + str(self.x) + " y:" + str(self.y) + " to (" + str(rval) +", " + str(gval) + ", " + str(bval) +") and sleeping for " + str(randval) + " seconds.")
            counter += 1
            sleep(randval)
            self.sense.set_pixel(x,y,0,0,0)
            sleep(5)
            self.sense.set_pixel(x,y,255,255,255)
            sleep(1)

        self.sense.set_pixel(x,y,0,0,0)
        self.endTime = time.time()
        data.append(round(self.endTime - self.startTime, 1)) 

        print("Exiting " + self.name + ". Lasted " + str(round(self.endTime - self.startTime, 2)) + " seconds")



sense = SenseHat()
sense.clear()

sense.low_light = True


data = []

for iteration in range(100):
    threads = []
    for i in range(8):
        for j in range(8):
            #print("i: " + str(i) + ", j: " + str(j) + " = " + str( (i * 8 ) + j + 1))
            thread = blinkThread((i * 8 ) + j + 1, "pixel " + str( (i * 8 ) + j + 1), 3, sense, i, j)
            threads.append(thread)

    for t in threads:
        t.start()
        #sleep(.001)

    for r in threads:
        r.join()
        #sleep(1)

    print ("Exiting Main Thread")


    bins = np.linspace(math.ceil(min(data)), math.floor(max(data)), 20) # fixed number of bins

    plt.xlim([min(data)-5, max(data)+5])

    plt.hist(data, bins=bins, alpha=0.5)
    plt.title('Random duration pixel changes over 50 iterations')
    plt.xlabel('variable X (seconds)')
    plt.ylabel('count')
    plt.savefig('iteration_' + str(iteration) + '.png')
    plt.clf()


bins = np.linspace(math.ceil(min(data)), math.floor(max(data)), 20) # fixed number of bins

plt.xlim([min(data)-5, max(data)+5])
plt.hist(data, bins=bins, alpha=0.5)
plt.title('Random duration pixel changes over 50 iterations')
plt.xlabel('variable X (seconds)')
plt.ylabel('count')
plt.savefig('iteration_final.png')
plt.show()
print("Done!")




        
