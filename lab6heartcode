import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math
import serial
import random

import re
import pygame
import matplotlib.patches as patches
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import matplotlib.image as image
import tkinter as tk
import tkinter.messagebox as messagebox


#initialixing pygame
pygame.init()
pygame.mixer.init()

lives_left = 3 #number of lives until game terminates
life_str = '❤'
#serious mode: only graphing
#non-serious mode flappy bird

#image for flappy bird icon
#reading this image 
file = "C:\\Users\\maya2\\Documents\\GitHub\\Lab6HeartRate\\heart-anatomy.png"
logo = image.imread(file)
#print(logo.shape); print(logo)

def on_option_select():
    selected = selected_option.get()
    result_label.config(text=f"Selected Option: {selected}")
root = tk.Tk()
root.title("Select your Heartrate Monitoring Mode")
root.geometry("400x100")
# Create a StringVar to hold the selected option
selected_option = tk.StringVar()
# Create the dropdown menu
options = ["Serious Mode", "Game Mode"]
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=10)
# Add a button to display the selected option
show_button = tk.Button(root, text="Show Selection", command=on_option_select)
show_button.pack()
# Label to display the selected option
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()

serious_flag = 0

if selected_option.get() == 'Serious Mode':
    serious_flag = 1
    print("Serious")

xsize=100 #must be multiple of 4!

avg_size = 10
xdata, y1data, y1avgdata = [], [], []


#noisebank!!!


for i in range(avg_size):
    y1data.append(80)



ser = serial.Serial(
    port='COM11', #change to whichever serial port we end up using (e.g. COM5)
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
        try:
            val1= float(strin[3:])
        except:
            print("nope")
            messagebox.showinfo("No Signal", "No signal detected! Please check your monitor connection.")
            sys.exit(0)

        yield t, val1


def run(data):  # Normal graph function (with averaging)
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

        

        if t>xsize: # Scroll to the left.
            ax.set_xlim(t-xsize, t)
    
        line1.set_data(xdata, y1data[10:])
        line2.set_data(xdata, y1avgdata)
        l1.get_texts()[0].set_text(f"Heartrate = {round(y1data[t+avg_size],2)} BPM")
        l2.get_texts()[0].set_text(f"Avg Heartrate = {round(y1avg,2)} BPM")

    return line1, line2,

def run_game(data): # Game graph function
    # update the data
    global ab
    t,y1 = data
    if t>-1:
        xdata.append(t)
        mody1 = y1
        if y1 > 250:
            y1data.append(y1data[t+avg_size])
            mody1 = y1data[t+avg_size]
        else:
            y1data.append(y1)
        
        ab.remove()
        
        # Create a new AnnotationBbox with the updated position
        imagebox = OffsetImage(logo, zoom=0.03)
        ab = AnnotationBbox(imagebox, (t, mody1), frameon=False)
        ax.add_artist(ab)

        if t>xsize/4:  # Scroll to the left.
            ax.set_xlim(t-xsize/4, t+3*xsize/4)
            t1.set_position(((t-xsize/4+3), 235))

        update_rects(rectlow1, recthigh1)
        update_rects(rectlow2, recthigh2)
        update_rects(rectlow3, recthigh3)
        update_rects(rectlow4, recthigh4)

        reset_rects(t, rectlow1, recthigh1)
        reset_rects(t, rectlow2, recthigh2)
        reset_rects(t, rectlow3, recthigh3)            
        reset_rects(t, rectlow4, recthigh4)            
        
        t1.set_text(f"Lives Left: {lives_left*life_str}")


        line1.set_data(xdata, y1data[10:])
        l1.get_texts()[0].set_text(f"{round(y1data[t+avg_size],2)} BPM")

        check_in_rects(t, mody1, rectlow1, recthigh1)
        check_in_rects(t, mody1, rectlow2, recthigh2)
        check_in_rects(t, mody1, rectlow3, recthigh3)
        check_in_rects(t, mody1, rectlow4, recthigh4)
    return line1, 


def update_rects(low_rec, high_rec): # shifts rects left 
    low_rec.set_x(low_rec.get_x()-1)
    high_rec.set_x(high_rec.get_x()-1)


def set_rect_height(low_rec, high_rec): # updates heights + space between rectangles randomly
    low_rec.set_height(random.randint(30,100))
    high_rec.set_y(low_rec.get_height() + random.randint(50,150)) #may need to modify rand

    
def reset_rects(t, low_rec, high_rec): #resets rects to right side and updates heights if it has been long enough 
    if (low_rec.get_x() < t - xsize/4 - random.randint(int(xsize/3)-5, int(xsize/3)+5)): 
        # location is set to right edge if rect is approx xsize/3 past the left edge
        # needs to be changed if we add more rectangles!
        low_rec.set_x(t+3*xsize/4)
        high_rec.set_x(t+3*xsize/4)
        low_rec.set_y(0)
        set_rect_height(low_rec, high_rec)


def check_in_rects(t, y1, low_rec, high_rec):  # check if curr val is in a rect set
    global lives_left
    if low_rec.get_x() <= t and low_rec.get_x() + low_rec.get_width() >= t:
        if y1 < low_rec.get_y() + low_rec.get_height():
            print("too low!!")
            low_rec.set_y(-200)
            lives_left -= 1
        if y1 > high_rec.get_y():
            print("too high!!")
            high_rec.set_y(250)
            lives_left -= 1
        if lives_left == 0:
            #add game over sequence
            
            print("dead")
            time.sleep(1)
            messagebox.showwarning("YOU DIED", f"Your score: {t}\nYour average heartrate: {round(sum(y1data[avg_size:])/(len(y1data)-avg_size),2)}")
            sys.exit(0)



def on_close_figure(event):
    sys.exit(0)



if serious_flag == 1: 
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

    #plt.imshow(logo)

    ani1 = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100, repeat=False)
    plt.show()

else:
    data_gen.t = -1
    fig = plt.figure()
    fig.canvas.mpl_connect('close_event', on_close_figure)
    ax = fig.add_subplot(111)
    line1, = ax.plot([], [], label='BPM', lw=2)
    ax.set_ylim(0, 250)
    ax.set_xlim(0, xsize)
    ax.set_ylabel('Heartrate (BPM)')
    l1 = ax.legend(handles = [line1], loc = 1)
    ax.add_artist(l1)

    t1 = ax.text(3,235,f"Lives left: {life_str*lives_left}", bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round',alpha=0.5))

    imagebox = OffsetImage(logo, zoom = 0.03)
    ab = AnnotationBbox(imagebox, (0, 80), frameon = False)
    ax.add_artist(ab)

    rectlow1 = patches.Rectangle((int(xsize*1/3), 0), 10, 50, linewidth=0, facecolor='steelblue')
    ax.add_patch(rectlow1)

    recthigh1 = patches.Rectangle((int(xsize*1/3), 200), 10, 250, linewidth=0, facecolor='steelblue')
    ax.add_patch(recthigh1)

    rectlow2 = patches.Rectangle((int(xsize*2/3), 0), 10, 50, linewidth=0, facecolor='crimson')
    ax.add_patch(rectlow2)

    recthigh2 = patches.Rectangle((int(xsize*2/3), 200), 10, 250, linewidth=0, facecolor='crimson')
    ax.add_patch(recthigh2)

    rectlow3 = patches.Rectangle((int(xsize*3/3), 0), 10, 50, linewidth=0, facecolor='lightblue')
    ax.add_patch(rectlow3)

    recthigh3 = patches.Rectangle((int(xsize*3/3), 200), 10, 250, linewidth=0, facecolor='lightblue')
    ax.add_patch(recthigh3)

    rectlow4 = patches.Rectangle((int(xsize*4/3), 0), 10, 50, linewidth=0, facecolor='palevioletred')
    ax.add_patch(rectlow4)

    recthigh4 = patches.Rectangle((int(xsize*4/3), 200), 10, 250, linewidth=0, facecolor='palevioletred')
    ax.add_patch(recthigh4)

    set_rect_height(rectlow1, recthigh1)
    set_rect_height(rectlow2, recthigh2)
    set_rect_height(rectlow3, recthigh3)  
    set_rect_height(rectlow4, recthigh4)  
    

    # rects are set up before we start - random heights and spaced correctly

    ani1 = animation.FuncAnimation(fig, run_game, data_gen, blit=False, interval=100, repeat=False)
    plt.show()
    
    # still set up same graph style (maybe no graph lines though)                                   ✓
    # could even still label with Heartrate (BPM)                                                   ✓
    
    # add recangles with random heights (two types at a time - top rect and bottom rect)            ✓
    # move them along graph (in run - should make separate run_game func)                           ✓
    # if the current t and BPM vals are in the rectangles, you lose                                 ✓
    # space between rectangles (how long to wait before adding a new one) can be somewhat random    ✓
    # height between rectangles can also be somewhat random                                         ✓
    # should start moving graph earlier, and keep location of current val towards beginning         ✓
    
    # look into having an image at the current val - you probably can have images on graphs  <-------------------

    # https://towardsdatascience.com/how-to-add-an-image-to-a-matplotlib-plot-in-python-76098becaf53
