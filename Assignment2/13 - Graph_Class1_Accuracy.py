#       About - Graph for class1 Accuracy
#       Updated             20/11/2015
#       Prerequisites - Data obtained from earlier runs collected and initialized
#       Output - Graph for class1 Accuracy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['legend.handlelength'] = 0

#Class 1 Data
x1 = [16866,1500,1000,500,400,200,100]
y1 = [96,96,96,94,94,94,94]

# use pylab to plot x and y
plt.plot(x1, y1, 'r-*', label = 'Class 1 Accuracy')

# set axis limits
plt.xlim(0.0, 17000.0)
plt.ylim(90.0, 100.0)

plt.xlabel('x axis - Dictionary Size')
plt.ylabel('y axis - Accuracy')
plt.title('Plot of Dictionary vs. Class 1 Accuracy of Prediction')

plt.legend(loc='best', numpoints=1)
plt.show()
