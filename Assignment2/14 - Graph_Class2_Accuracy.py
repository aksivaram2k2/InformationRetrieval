#       About - Graph for class2 Accuracy
#       Updated             20/11/2015
#       Prerequisites - Data obtained from earlier runs collected and initialized
#       Output - Graph for class2 Accuracy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['legend.handlelength'] = 0

#Class 2 Data
x2 = [16866,1500,1000,500,400,200,100]
y2 = [96,96,96,96,96,92,94]

# use pylab to plot x and y
plt.plot(x2, y2, 'g-^', label = 'Class 2 Accuracy')

# set axis limits
plt.xlim(0.0, 17000.0)
plt.ylim(90.0, 100.0)

plt.xlabel('x axis - Dictionary Size')
plt.ylabel('y axis - Accuracy')
plt.title('Plot of Dictionary vs. Class 2   Accuracy of Prediction')

plt.legend(loc='best', numpoints=1)
plt.show()
