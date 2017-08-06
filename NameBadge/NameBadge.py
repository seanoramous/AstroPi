from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

while True:
    for poll in range(50):
        #orientation = sense.get_orientation()
        acceleration = sense.get_accelerometer_raw()
        
    #pitch = round(orientation['pitch'])
    #roll = round(orientation['roll'])
    #yaw = round(orientation['yaw'])

    xaxis = round(acceleration['x'])
    yaxis = round(acceleration['y'])
    zaxis = round(acceleration['z'])
            
    if yaxis==-1:
        sense.set_rotation(180)
    elif xaxis == 1:
        sense.set_rotation(270)
    elif xaxis == -1:
        sense.set_rotation(90)
    else:
        sense.set_rotation(0)

    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    #sense.show_message("pitch={0}, roll={1}, yaw = {2}".format(pitch,roll,yaw))

    #sense.clear((r,g,b))

    #sleep(2)

    #sense.clear((r,g,0))

    #sleep(.5)

    #sense.clear((r,0,b))

    #sleep(.5)
    
    #sense.clear((0,g,b))

    #sleep(.5)

    #sense.clear((r,0,0))

    #sleep(.5)

    #sense.clear((0,g,0))

    #sleep(.5)

    #sense.clear((0,0,b))

    #sleep(.5)

    #sense.clear((0,0,0))

    #sleep(2)

    #sense.show_message("Sean Oramous", text_colour=(r,0,0))

    #sense.clear((r,g,b))

    #sleep(2)

    sense.show_message("Sean Oramous", text_colour=(r,g,0), back_colour=(0,0,b))

    sense.clear((r,g,b))
    sleep(.5)
    #x = 0
    #y = 0

    #sense.set_pixel(x,y,r,g,b)

    sense.clear((0,0,0))
    sleep(1)
    
    for i in range(randint(1,100)):
        x = randint(0,7)
        y = randint(0,7)
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        sense.set_pixel(x,y,r,g,b)
        sleep(0.1)

    sense.clear((0,0,0))
    #sense.temperature
    #for i in range(randint(9,60),0,-1):
        #sense.show_letter(str(i // 10))
        #sleep(.3)
        #sense.clear((0,0,0))
        #sleep(.2)
        #sense.show_letter(str(i % 10))
        #sleep(.4)
        #sense.clear((0,0,0))
        #sleep(.4)
    sleep(randint(0,60))
        
    #for j in range(0, 360, 90):
        #sense.show_letter("S")
        #sense.set_rotation(j)
        #sleep(.2)
