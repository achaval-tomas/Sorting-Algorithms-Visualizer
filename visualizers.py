import pygame as py

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
    # Create deep copies of two halves of the array
    L, R = [], []
    for i in range(mid - lft + 1):
        L.append(arr[lft + i])
    for j in range(rgt - mid):
        R.append(arr[mid + 1 + j])

    # These two values will act as stoppers
    L.append(100000); R.append(100000)

    i, j = 0, 0
    for k in range(lft, rgt+1):
        drawrect(k, arr, scr, "black")
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        drawrect(k, arr, scr, "blue")
        py.time.delay(5)
    
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