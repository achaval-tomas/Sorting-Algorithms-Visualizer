import pygame as py
from math import floor

def greenPass(arr, scr):
    l = len(arr)
    for i in range(l):
        drawrect(i, arr, scr, "green")
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
    elif sort == 3:
        mergeSort(arr, scr)
    greenPass(arr, scr)
    return

# Draw the rectangle that corresponds to array[r] with any color.
def drawrect(r, array, screen, color):
    h = array[r]
    py.draw.rect(screen, color, py.Rect(20+r*5, 780-h*3, 4, h*3))
    py.display.flip()
    return

def whitearr(array, screen):
    l = len(array)
    screen.fill("black")
    for i in range(l):
        h = array[i]
        py.draw.rect(screen, "white", py.Rect(20+i*5, 780-h*3, 4, h*3))
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
        drawrect(piv, arr, scr, "green")
        py.time.delay(20)
        qsort(arr, lft, piv, scr)
        qsort(arr, piv+1, rgt, scr)
    return

def quickSort(array, scr):
    qsort(array, 0, len(array), scr)
    return


def merge(arr, lft, mid, rgt, scr):
    n1 = mid - lft + 1
    n2 = rgt - mid
 
    # Create deep copies of two halves of the array
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[lft + i]
 
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
    
    i, j, k = 0, 0, lft

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        drawrect(k, arr, scr, "blue")
        py.time.delay(5)
        k+=1
    
    while i<n1:
        arr[k] = L[i]
        drawrect(k, arr, scr, "blue")
        k+=1; i+=1
    while j<n2:
        arr[k] = R[j]
        drawrect(k, arr, scr, "blue")
        k+=1; j+=1

    return

def mSort(arr, lft, rgt, scr):
    if lft < rgt:
        mid = (lft+rgt)//2
        mSort(arr, lft, mid, scr)
        mSort(arr, mid+1, rgt, scr)
        merge(arr, lft, mid, rgt, scr)
        whitearr(arr, scr)
        py.time.delay(20)
    return


def mergeSort(array, scr):
    mSort(array, 0, len(array)-1, scr)
    return