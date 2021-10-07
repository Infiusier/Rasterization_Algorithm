# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt 
from cv2 import data

MAX_SIZE_WIDTH = 100
MAX_SIZE_LENGTH = 100

POINT_1 = [0,0]
POINT_2 = [65,12]

def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
 
    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    #error = int(dx / 2.0)
    error = 6
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

if __name__=='__main__':
    line = [POINT_1,POINT_2]

    # data[y][x] onde Y é a linha e X a coluna
    data = np.zeros((MAX_SIZE_LENGTH,MAX_SIZE_WIDTH,1))
    
    for point in get_line(line[0],line[1]): 
        try:
            data[point[1]][point[0]] = 255
        except:
            pass
    
    plt.imshow(data,'gray',origin='lower',extent=(0, MAX_SIZE_WIDTH, 0, MAX_SIZE_LENGTH))
    plt.plot([line[0][0],line[1][0]],[line[0][1],line[1][1]],linestyle='-');
    plt.show()
    

    