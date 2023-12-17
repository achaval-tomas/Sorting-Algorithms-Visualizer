import pygame as py

def visualize(sort, arr, scr):
    whitearr(arr, scr)
    if sort == 0:
        insertionSort(arr, scr)
    elif sort == 1:
        insertionSort(arr, scr)
    elif sort == 2:
        quickSort(arr)
    return

def drawrect(r, array, screen, color):
    h = array[r]
    py.draw.rect(screen, color, py.Rect(50+r*10, 700-h*6, 9, h*6))
    py.display.flip()
    return

def whitearr(array, screen):
    l = len(array)
    screen.fill("black")
    for i in range(l):
        h = array[i]
        py.draw.rect(screen, "white", py.Rect(50+i*10, 700-h*6, 9, h*6))
    py.display.flip()
    return

def swap(arr, i, j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def selectionSort(array, scr):
    l = len(array)
    for i in range(l):
        m = i
        for j in range(i, l):
            drawrect(j, array, scr, "blue")
            if array[j] <= array[m]:
                m = j
                drawrect(m, array, scr, "green")
            py.time.delay(10)
            if m != j:
                drawrect(j, array, scr, "white")
        swap(array, i, m)
        whitearr(array, scr)

    return

def insertionSort(array, scr):
    l = len(array)

    for i in range(1, l):
        pos = i
        while pos > 0 and array[pos] < array[pos-1]:
            drawrect(pos, array, scr, "green")
            swap(array, pos, pos-1)
            py.time.delay(10)
            pos -= 1
            whitearr(array, scr)

    return

def quickSort(array):
    return