import pygame as py

py.font.init()
my_font = py.font.SysFont('Comic Sans MS', 30)
comparisons = 0
array_access = 0
sort_alg = ""

def greenPass(arr, scr):
    l = len(arr)
    for i in range(l):
        drawrect(i, arr, scr, "green")
        py.time.delay(10)
    return

def visualize(sort, arr, scr):
    global comparisons, array_access, sort_alg
    comparisons = 0
    array_access = 0

    if sort == 0:
        sort_alg = "Selection"
        whitearr(arr, scr)
        selectionSort(arr, scr)
    elif sort == 1:
        sort_alg = "Insertion"
        whitearr(arr, scr)
        insertionSort(arr, scr)
    elif sort == 2:
        sort_alg = "Quick"
        whitearr(arr, scr)
        quickSort(arr, scr)
    elif sort == 3:
        sort_alg = "Merge"
        whitearr(arr, scr)
        mergeSort(arr, scr)
    elif sort == 4:
        sort_alg = "Bubble"
        whitearr(arr, scr)
        bubbleSort(arr, scr)

    greenPass(arr, scr)
    return

def printStats(scr):
    stats = my_font.render("{} Sort, Comparisons: {}, Array Accesses: {}".format(sort_alg, comparisons, array_access), False, "white")
    scr.blit(stats, (5,5))

# Draw the rectangle that corresponds to array[r] with any color.
def drawrect(r, array, screen, color):
    h = array[r]
    py.draw.rect(screen, color, py.Rect(15+r*5, 780-h*3, 4, h*3))
    py.display.flip()
    return

def whitearr(array, screen):
    l = len(array)
    screen.fill("black")
    printStats(screen)
    for i in range(l):
        h = array[i]
        py.draw.rect(screen, (255-h/3, 255-h/2, h), py.Rect(15+i*5, 780-h*3, 4, h*3))
    py.display.flip()
    return

# Aux
def swap(arr, i, j):
    global array_access
    array_access += 4
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

'''                          SORTING ALGORITHMS                        '''
def selectionSort(array, scr):
    global comparisons, array_access
    n = len(array)
    for i in range(n):
        m = i
        for j in range(i, n):
            if array[j] <= array[m]:
                m = j

            comparisons += 1
            array_access += 2

        drawrect(m, array, scr, "green")
        py.time.delay(50)
        swap(array, i, m)
        whitearr(array, scr)
        drawrect(i, array, scr, "blue")
        py.time.delay(20)

    return


def insertionSort(array, scr):
    global comparisons, array_access
    l = len(array)

    for i in range(1, l):
        pos = i
        while pos > 0 and array[pos] < array[pos-1]:
            swap(array, pos, pos-1)
            pos -= 1
            comparisons += 1
            array_access += 2
        whitearr(array, scr)
        drawrect(pos, array, scr, "green")
        py.time.delay(20)

    return


def partition(arr, lft, rgt, scr):
    global comparisons, array_access
    piv = lft
    drawrect(piv, arr, scr, "green")
    for i in range(lft+1, rgt):
        if arr[i] < arr[lft]:
            drawrect(i, arr, scr, "blue")
            piv += 1
            swap(arr, i, piv)
        else:
            drawrect(i, arr, scr, "red")
        
        array_access += 2
        comparisons += 1
        py.time.delay(5)

    swap(arr, lft, piv)
    return piv

def qsort(arr, lft, rgt, scr):
    if (lft < rgt):
        piv = partition(arr, lft, rgt, scr)
        whitearr(arr, scr)
        py.time.delay(20)
        qsort(arr, lft, piv, scr)
        qsort(arr, piv+1, rgt, scr)
    return

def quickSort(array, scr):
    qsort(array, 0, len(array), scr)
    return


def merge(arr, lft, mid, rgt, scr):
    global comparisons, array_access
    # Create deep copies of two halves of the array
    L, R = [], []
    for i in range(mid - lft + 1):
        L.append(arr[lft + i])
    for j in range(rgt - mid):
        R.append(arr[mid + 1 + j])
    array_access += (rgt-lft+1)

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
        comparisons += 1
        array_access += 4
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


def bubbleSort(array, scr):
    global comparisons, array_access
    n = len(array)
    for i in range(1,n):
        for j in range(n-i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
            comparisons += 1
            array_access += 2
        whitearr(array, scr)
        drawrect(n-i, array, scr, "blue")
        py.time.delay(30)
    return