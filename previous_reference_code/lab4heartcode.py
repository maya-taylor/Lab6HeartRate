
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math
import serial

import re
import pygame

#initialixing pygame
pygame.init()
pygame.mixer.init()

#whale
whale_file = "C:\\Users\\maya2\\Desktop\\lab4sounds\\whalesound.mp3"
whale = pygame.mixer.Sound(whale_file)
#elephant
elephant_file = "C:\\Users\\maya2\\Desktop\\lab4sounds\\elephantsound.mp3"
elephant = pygame.mixer.Sound(elephant_file)
#cow
cow_file = "C:\\Users\\maya2\\Desktop\\lab4sounds\\cowsound.mp3"
cow = pygame.mixer.Sound(cow_file)
#horse
horse_file ="C:\\Users\\maya2\\Desktop\\lab4sounds\\horsesound.mp3"
horse = pygame.mixer.Sound(horse_file)
#dog
dog_file = "C:\\Users\\maya2\\Desktop\\lab4sounds\\dogsound.mp3"
dog = pygame.mixer.Sound(dog_file)
#pig
pig_file ="C:\\Users\\maya2\\Desktop\\lab4sounds\\pigsound.mp3"
pig = pygame.mixer.Sound(pig_file)
#monkey
monkey_file = "C:\\Users\\maya2\\Desktop\\lab4sounds\\monkeysound.mp3"
monkey = pygame.mixer.Sound(monkey_file)
#cat
cat_file = "C:\\Users\\maya2\\Desktop\\lab4sounds\\catsound.mp3"
cat = pygame.mixer.Sound(cat_file)
#mouse
mouse_file = "C:\\Users\\maya2\\Desktop\\lab4sounds\\mousesound.mp3"
mouse = pygame.mixer.Sound(mouse_file)
xsize=100

avg_size = 10
xdata, y1data, y1avgdata = [], [], []
animal = "pig"
whale_flag = 0
elephant_flag = 0
cow_flag = 0
horse_flag = 0
dog_flag = 0
pig_flag = 0
monkey_flag = 0
cat_flag = 0
mouse_flag = 0

whale_flag2 = 0
elephant_flag2 = 0
cow_flag2 = 0
horse_flag2 = 0
dog_flag2 = 0
pig_flag2 = 0
monkey_flag2 = 0
cat_flag2 = 0
mouse_flag2 = 0

#noisebank!!!


for i in range(avg_size):
    y1data.append(80)



ser = serial.Serial(
    port='COM19', #change to whichever serial port we end up using (e.g. COM5)
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()    


def data_gen():
    t = data_gen.t
    while True:
        strin = ser.readline()
        print(strin) 
        t+=1
        val1= float(strin[0:9])
        yield t, val1


def run(data):
    global animal, whale_flag,elephant_flag, cow_flag,horse_flag,dog_flag, pig_flag, monkey_flag,cat_flag,mouse_flag
    global whale_flag2,elephant_flag2, cow_flag2,horse_flag2,dog_flag2, pig_flag2, monkey_flag2,cat_flag2,mouse_flag2
    # update the data
    t,y1 = data
    if t>-1:
        xdata.append(t)
        if y1 > 250:
            y1data.append(y1data[t+avg_size])
        else:
            y1data.append(y1)

        y1avg = np.sum(y1data[t:t+avg_size])/avg_size
        y1avgdata.append(y1avg)

                    
        #whale
        if y1avg < 30:
            #reseting flags of the other animals
            elephant_flag = 0
            cow_flag = 0
            horse_flag = 0
            dog_flag = 0
            pig_flag = 0
            monkey_flag = 0
            cat_flag = 0
            mouse_flag = 0

            #whale_flag2 = 0
            elephant_flag2 = 0
            cow_flag2 = 0
            horse_flag2 = 0
            dog_flag2 = 0
            pig_flag2 = 0
            monkey_flag2 = 0
            cat_flag2 = 0
            mouse_flag2 = 0

            animal  = "whale"
            if whale_flag != 1:
                #set up whale noise here
                if whale_flag2 == 0:
                    whale_flag2 = 1
                else:
                    whale.play()
                    whale_flag2 = 0
                    whale_flag = 1

            

        #elephant
        if y1avg >= 30 and y1avg < 50:
            whale_flag = 0
            #elephant_flag = 0
            cow_flag = 0
            horse_flag = 0
            dog_flag = 0
            pig_flag = 0
            monkey_flag = 0
            cat_flag = 0
            mouse_flag = 0

            whale_flag2 = 0
            #elephant_flag2 = 0
            cow_flag2 = 0
            horse_flag2 = 0
            dog_flag2 = 0
            pig_flag2 = 0
            monkey_flag2 = 0
            cat_flag2 = 0
            mouse_flag2 = 0

            animal = "elephant"
            if elephant_flag != 1:
                #set up elephant noise
                if elephant_flag2 == 0:
                    elephant_flag2 = 1
                else:
                    elephant.play()
                    elephant_flag2 = 0
                    elephant_flag = 1
        
        #cow 
        if y1avg >= 50 and y1avg < 60:
            whale_flag = 0
            elephant_flag = 0
            #cow_flag = 0
            horse_flag = 0
            dog_flag = 0
            pig_flag = 0
            monkey_flag = 0
            cat_flag = 0
            mouse_flag = 0

            whale_flag2 = 0
            elephant_flag2 = 0
            #cow_flag2 = 0
            horse_flag2 = 0
            dog_flag2 = 0
            pig_flag2 = 0
            monkey_flag2 = 0
            cat_flag2 = 0
            mouse_flag2 = 0

            animal = "cow"
            if cow_flag != 1:
                #set up cow noise
                if cow_flag2 == 0:
                    cow_flag2 = 1
                else:
                    cow.play()
                    cow_flag2 = 0
                    cow_flag = 1
        
        #horse
        if y1avg >= 60 and y1avg < 70:
            whale_flag = 0
            elephant_flag = 0
            cow_flag = 0
            #horse_flag = 0
            dog_flag = 0
            pig_flag = 0
            monkey_flag = 0
            cat_flag = 0
            mouse_flag = 0

            whale_flag2 = 0
            elephant_flag2 = 0
            cow_flag2 = 0
            #horse_flag2 = 0
            dog_flag2 = 0
            pig_flag2 = 0
            monkey_flag2 = 0
            cat_flag2 = 0
            mouse_flag2 = 0

            animal = "horse"
            if horse_flag != 1:
                #set up cow noise
                if horse_flag2 == 0:
                    horse_flag2 = 1
                else:
                    horse.play()
                    horse_flag2 = 0
                    horse_flag = 1

        #dog
        if y1avg >= 70 and y1avg < 80:
            #reseting flags of the other animals
            whale_flag = 0
            elephant_flag = 0
            cow_flag = 0
            horse_flag = 0
            pig_flag = 0
            monkey_flag = 0
            cat_flag = 0
            mouse_flag = 0

            whale_flag2 = 0
            elephant_flag2 = 0
            cow_flag2 = 0
            horse_flag2 = 0
            #dog_flag2 = 0
            pig_flag2 = 0
            monkey_flag2 = 0
            cat_flag2 = 0
            mouse_flag2 = 0

            animal  = "dog"
            if dog_flag != 1:
                #set up whale noise here
                if dog_flag2 == 0:
                    dog_flag2 = 1
                else:
                    dog_flag2 = 0
                    dog.play()
                    dog_flag = 1

        #pig
        if y1avg >= 80 and y1avg < 90:
            #reseting flags of the other animals
            whale_flag = 0
            elephant_flag = 0
            cow_flag = 0
            horse_flag = 0
            dog_flag = 0
            #pig_flag = 0
            monkey_flag = 0
            cat_flag = 0
            mouse_flag = 0

            whale_flag2 = 0
            elephant_flag2 = 0
            cow_flag2 = 0
            horse_flag2 = 0
            dog_flag2 = 0
            #pig_flag2 = 0
            monkey_flag2 = 0
            cat_flag2 = 0
            mouse_flag2 = 0

            animal  = "pig"
            if pig_flag != 1:
                #set up whale noise here
                if pig_flag2 == 0:
                    pig_flag2 = 1
                else:
                    pig_flag2 = 0
                    pig.play()
                    pig_flag = 1   

        #monkey
        if y1avg >= 90 and y1avg < 100:
            #reseting flags of the other animals
            whale_flag = 0
            elephant_flag = 0
            cow_flag = 0
            horse_flag = 0
            pig_flag = 0
            #monkey_flag = 0
            cat_flag = 0
            mouse_flag = 0

            whale_flag2 = 0
            elephant_flag2 = 0
            cow_flag2 = 0
            horse_flag2 = 0
            dog_flag2 = 0
            pig_flag2 = 0
            #monkey_flag2 = 0
            cat_flag2 = 0
            mouse_flag2 = 0

            animal  = "monkey"
            if monkey_flag != 1:
                #set up whale noise here
                if monkey_flag2 == 0:
                    monkey_flag2 = 1
                else:
                    monkey.play()
                    monkey_flag2 = 0
                    monkey_flag = 1      
            
        #cat
        if y1avg >= 100 and y1avg < 110:
            #reseting flags of the other animals
            whale_flag = 0
            elephant_flag = 0
            cow_flag = 0
            horse_flag = 0
            pig_flag = 0
            monkey_flag = 0
            #cat_flag = 0
            mouse_flag = 0

            whale_flag2 = 0
            elephant_flag2 = 0
            cow_flag2 = 0
            horse_flag2 = 0
            dog_flag2 = 0
            pig_flag2 = 0
            monkey_flag2 = 0
            #cat_flag2 = 0
            mouse_flag2 = 0

            animal  = "cat"
            if cat_flag != 1:
                #set up whale noise here
                if cat_flag2 == 0:
                    cat_flag2 = 1
                else:
                    cat_flag2 = 0
                    cat.play()
                    cat_flag = 1    

            #mouse
        if y1avg >= 110:
            #reseting flags of the other animals
            whale_flag = 0
            elephant_flag = 0
            cow_flag = 0
            horse_flag = 0
            pig_flag = 0
            monkey_flag = 0
            cat_flag = 0
            #mouse_flag = 0

            whale_flag2 = 0
            elephant_flag2 = 0
            cow_flag2 = 0
            horse_flag2 = 0
            dog_flag2 = 0
            pig_flag2 = 0
            monkey_flag2 = 0
            cat_flag2 = 0
            #mouse_flag2 = 0

            animal  = "mouse"

            if mouse_flag != 1:
                #set up whale noise here
                if mouse_flag2 == 0:
                    mouse_flag2 = 1
                else:
                    mouse_flag2 = 0
                    mouse.play()
                    mouse_flag = 1  
        

        if t>xsize: # Scroll to the left.
            ax.set_xlim(t-xsize, t)
            t1.set_position(((t-xsize+10), 220))
        line1.set_data(xdata, y1data[10:])
        line2.set_data(xdata, y1avgdata)
        l1.get_texts()[0].set_text(f"Heartrate = {round(y1data[t+avg_size],2)} BPM")
        l2.get_texts()[0].set_text(f"Avg Heartrate = {round(y1avg,2)} BPM")
        t1.set_text(f"You are a: {animal}")
    return line1, line2,


def on_close_figure(event):
    sys.exit(0)


data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line1, = ax.plot([], [], label='BPM', lw=2)
line2, = ax.plot([], [], label='BPMavg', lw=2)
ax.set_ylim(0, 250)
ax.set_xlim(0, xsize)
ax.set_xlabel('Readings')
ax.set_ylabel('Heartrate (BPM)')
ax.set_title('Heartrate over Time')
ax.grid()
l1 = ax.legend(handles = [line1], loc = 1)
ax.add_artist(l1)
l2 = ax.legend(handles=[line2], loc = 4)
t1 = ax.text(10,220,f"You are a: {animal}", bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round',alpha=0.5))

ani1 = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100, repeat=False)
plt.show()
