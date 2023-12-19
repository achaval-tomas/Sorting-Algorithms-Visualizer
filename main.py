import pygame as py
from random import randint
from visualizers import *

width, height = 1280, 800

py.init()
screen = py.display.set_mode((width, height))
py.display.set_caption('Sorting Algorithms Visualizer')

arr = [i+1 for i in range(250)]
def resetArray():
    global arr
    for _ in range(500):
        a, b = randint(0, 249), randint(0, 249)
        aux = arr[a]
        arr[a] = arr[b]
        arr[b] = aux
    return

# initial sort [SELECTION, INSERTION, QUICK, MERGE]
sort = -1
resetArray()
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
    elif keys[py.K_b]:
        return 4
    elif keys[py.K_r]:
        resetArray()
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