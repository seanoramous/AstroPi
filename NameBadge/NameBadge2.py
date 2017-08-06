from sense_hat import SenseHat
from time import sleep
#import random
from random import randint
import threading
import time
import subprocess

exitFlag = 0

class orientationThread (threading.Thread):
    def __init__(self, threadID, name, counter, sense):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.sense = sense
    def run(self):
        print("Starting " + self.name)

        while True:
              
            for poll in range(5):
             acceleration = self.sense.get_accelerometer_raw()
        
            xaxis = round(acceleration['x'])
            yaxis = round(acceleration['y'])
            zaxis = round(acceleration['z'])

            #print("x={0}, y={1}, z={2}".format(xaxis, yaxis, zaxis))
            
            if xaxis==-1:
                rotation = 0
            elif yaxis == 1:
                rotation = 270
            elif yaxis == -1:
                rotation = 90
            else:
                rotation = 180

 
            self.sense.set_rotation(rotation, True)
            #print(rotation)
                
            #time.sleep(.1)

        print("Exiting " + self.name)

class nameThread (threading.Thread):
    def __init__(self, threadID, name, counter, sense):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.sense = sense
    def run(self):
        print("Starting " + self.name)
        while True:
              
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)

            #threadLock.acquire()

            #if random.random() > .9:
            #    print("This far")
            #    result = subprocess.check_output(['fortune','off/atheism'])
            #    r = result.decode("utf-8")
            #    self.sense.show_message(r, scroll_speed=0.1, text_colour=(r,g,0), back_colour = (0,0,b))
            #else:
            self.sense.show_message("Sean Oramous", scroll_speed=0.1, text_colour=(r,g,0), back_colour=(0,0,b))

            #self.sense.clear((r,g,b))
            #sleep(.5)

            #self.sense.clear((0,0,0))
            #sleep(1)
            
            for i in range(randint(1,1000)):
                x = randint(0,7)
                y = randint(0,7)
                r = randint(0,255)
                g = randint(0,255)
                b = randint(0,255)
                self.sense.set_pixel(x,y,r,g,b)
                sleep(0.01)

            #self.sense.clear((0,0,0))
            #threadLock.release()
            #sleep(randint(0,60))

        print("Exiting " + self.name)

class rpiThread (threading.Thread):
    def __init__(self, threadID, name, counter, sense):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.sense = sense
    def run(self):
        print("Starting " + self.name)

              
        r = (255, 0, 0)
        o = (255, 127, 0)
        y = (255, 255, 0)
        g = (0, 255, 0)
        b = (0, 0, 255)
        i = (75, 0, 130)
        v = (159, 0, 255)
        e = (0, 0, 0)


        image = [
        e,e,e,e,e,e,e,e,
        e,e,e,r,r,e,e,e,
        e,r,r,o,o,r,r,e,
        r,o,o,y,y,o,o,r,
        o,y,y,g,g,y,y,o,
        y,g,g,b,b,g,g,y,
        b,b,b,i,i,b,b,b,
        b,i,i,v,v,i,i,b
        ]


        image = [
        e,e,e,r,r,e,e,e,
        e,e,r,r,r,r,e,g,
        e,r,r,r,r,r,g,g,
        r,r,r,r,r,r,g,e,
        r,r,r,r,r,r,g,e,
        e,r,r,r,r,r,g,g,
        e,e,r,r,r,r,e,g,
        e,e,e,r,r,e,e,e
        ]



        #threadLock.acquire()




        self.sense.set_pixels(image)
        self.sense.set_rotation(90)
        #sleep(200)
        #threadLock.release()

        print("Exiting " + self.name)


#threadLock = threading.Lock()

sense = SenseHat()

rpi = rpiThread(1, "Raspberry Pi Image", 3, sense)
rpi.start()
rpi.join()

OrientThread = orientationThread(2,"OrientThread", 3, sense)
OrientThread.start()
OrientThread.join()

name = nameThread(3, "NameBadge", 3, sense)

sleep(60)

name.start()
nameThread.join()


print ("Exiting Main Thread")





        
