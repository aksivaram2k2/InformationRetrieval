#       About - Graph for Ties
#       Updated             20/11/2015
#       Prerequisites - Data obtained from earlier runs collected and initialized
#       Output - Graph for Ties

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['legend.handlelength'] = 0

#Class 1 Data
x1 = [16866,1500,1000,500,400,200,100]
y1 = [0,0,0,0,0,0,0]

# use pylab to plot x and y
plt.plot(x1, y1, 'r-*', label = 'Number of Ties')

# set axis limits
plt.xlim(0.0, 17000.0)
plt.ylim(-1, 1)

plt.xlabel('x axis - Dictionary Size')
plt.ylabel('y axis - Accuracy')
plt.title('Plot of Dictionary vs. Number of Ties')

plt.legend(loc='best', numpoints=1)
plt.show()
