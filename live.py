import copy
import time
import matplotlib.pyplot as plt

plt.ion()

startPosition = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

h = len(startPosition)
w = len(startPosition[0])

height = range(h)
width = range(w)


def createMatrix(height, width, matrix):
    for h in range(height):
        matrix.append([])
        for w in range(width):
            matrix[h].append(0)



def getField(i,j, field):
    if i == -1: i= len(field)-1
    if j == -1: j = len(field[0])-1
    if i == len(field): i = 0
    if j == len(field[0]): j = 0
    return field[i][j]

def numberOfNeighbor(i, j, field):
    count = 0

    for ii in range(i - 1, i + 1+1):
        for jj in range(j - 1, j + 1+1):
            if not (ii == i and jj == j):
                if getField(ii, jj, field): count += 1
    return count



field = copy.deepcopy(startPosition)
gen = 0;

while True:
    tmpField = []
    createMatrix(h, w, tmpField)
    for hh in height:
        for ww in width:
            if field[hh][ww] and (numberOfNeighbor(hh, ww, field) == 2 or numberOfNeighbor(hh, ww, field) == 3):
                tmpField[hh][ww] = 1
                continue
            if not field[hh][ww] and numberOfNeighbor(hh, ww, field) == 3:
                tmpField[hh][ww] = 1
                continue
            if field[hh][ww] and numberOfNeighbor(hh, ww, field) > 3:
                tmpField[hh][ww] = 0
                continue

    #print('generation: {}'.format(gen))
    #gen += 1
    #for i in height:
    #    print (tmpField[i])
    plt.imshow(tmpField)
    field = copy.deepcopy(tmpField)
    plt.pause(0.1)


