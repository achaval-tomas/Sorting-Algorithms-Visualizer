import pygame as py
from random import randrange
from visualizers import *

width, height = 1280, 720

py.init()
screen = py.display.set_mode((width, height))
py.display.set_caption('Sorting Algorithms Visualizer')

# initial sort [SELECTION, INSERTION, QUICK]
sort = 0

# handle key inputs
def keyActions():
    keys = py.key.get_pressed()
    if keys[py.K_s]:
        sort = 0
    elif keys[py.K_i]:
        sort = 1
    return

arr = []
def resetArray(array):
    array.clear()
    for i in range(1, 100):
        array.insert(randrange(0, 99), i)
    return

# initialize loop properties
clock = py.time.Clock()
running = True
framerate = 60

'''                                 MAIN LOOP                                       '''
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    resetArray(arr)

    keyActions()                            # handle key inputs

    visualize(sort, arr, screen)
    
    py.display.flip()                   # display all renders on screen

    clock.tick(framerate)

py.quit()