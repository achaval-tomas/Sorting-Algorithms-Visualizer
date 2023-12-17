import pygame as py

def greenPass(arr, scr):
    l = len(arr)
    for i in range(l):
        h = arr[i]
        py.draw.rect(scr, "green", py.Rect(20+i*5, 700-h*2.5, 4, h*2.5))
        py.display.flip()
        py.time.delay(10)
    return

def visualize(sort, arr, scr):
    whitearr(arr, scr)
    if sort == 0:
        selectionSort(arr, scr)
    elif sort == 1:
        insertionSort(arr, scr)
    elif sort == 2:
        quickSort(arr, scr)
    greenPass(arr, scr)
    return

# Draw the rectangle that corresponds to array[r] with any color.
def drawrect(r, array, screen, color):
    h = array[r]
    py.draw.rect(screen, color, py.Rect(20+r*5, 700-h*2.5, 4, h*2.5))
    py.display.flip()
    return

def whitearr(array, screen):
    l = len(array)
    screen.fill("black")
    for i in range(l):
        h = array[i]
        py.draw.rect(screen, "white", py.Rect(20+i*5, 700-h*2.5, 4, h*2.5))
    py.display.flip()
    return

# Aux
def swap(arr, i, j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

'''                          SORTING ALGORITHMS                        '''
def selectionSort(array, scr):
    l = len(array)
    for i in range(l):
        m = i
        for j in range(i, l):
            drawrect(j, array, scr, "blue")
            if array[j] <= array[m]:
                m = j
                drawrect(m, array, scr, "green")
                py.time.delay(5)
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
            py.time.delay(5)
            pos -= 1
            whitearr(array, scr)

    return

def partition(arr, lft, rgt, scr):
    piv = lft
    for i in range(lft+1, rgt):
        if arr[i] < arr[lft]:
            piv += 1
            swap(arr, i, piv)
    swap(arr, lft, piv)
    return piv

def qsort(arr, lft, rgt, scr):
    if (lft < rgt):
        piv = partition(arr, lft, rgt, scr)
        whitearr(arr, scr)
        drawrect(piv, arr, scr, "blue")
        py.time.delay(20)
        qsort(arr, lft, piv, scr)
        qsort(arr, piv+1, rgt, scr)
    return

def quickSort(array, scr):
    qsort(array, 0, len(array), scr)
    return