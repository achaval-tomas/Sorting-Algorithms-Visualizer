import pygame as py
from random import randint
from visualizers import *

width, height = 1280, 800

py.init()
screen = py.display.set_mode((width, height))
py.display.set_caption('Sorting Algorithms Visualizer')

arr = []
def resetArray(array):
    array.clear()
    for i in range(250):
        array.append(i+1)
    for i in range(500):
        swap(arr, randint(0, 249), randint(0, 249))
    return

# initial sort [SELECTION, INSERTION, QUICK, MERGE]
sort = -1
resetArray(arr)
whitearr(arr, screen)

# handle key inputs
def keyActions():
    keys = py.key.get_pressed()
    if keys[py.K_s]:
        return 0
    elif keys[py.K_i]:
        return 1
    elif keys[py.K_q]:
        return 2
    elif keys[py.K_m]:
        return 3
    elif keys[py.K_r]:
        resetArray(arr)
        whitearr(arr, screen)
    return -1

# initialize loop properties
clock = py.time.Clock()
running = True
framerate = 60

'''                                 MAIN LOOP                                       '''
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    sort = keyActions()                 # handle key inputs to select sorting algorithm

    if sort != -1:
        visualize(sort, arr, screen)
        whitearr(arr, screen)
        sort = -1
    
    py.display.flip()                   # display all renders on screen

    clock.tick(framerate)

py.quit()