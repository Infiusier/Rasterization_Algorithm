
import numpy as np
import matplotlib.pyplot as plt 

MAX_SIZE_WIDTH = 10
MAX_SIZE_LENGTH = 10

POINT_1 = [0,0]
POINT_2 = [10,10]

line = [POINT_1,POINT_2]

data = np.zeros((MAX_SIZE_LENGTH,MAX_SIZE_WIDTH,1))

data[0][0] = 255


plt.imshow(data,'gray',origin='lower',extent=(0, MAX_SIZE_WIDTH, 0, MAX_SIZE_LENGTH))

plt.plot([line[0][0],line[1][0]],[line[0][1],line[1][1]],linestyle='-');

plt.show()