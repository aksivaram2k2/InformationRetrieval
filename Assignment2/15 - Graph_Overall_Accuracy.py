#       About - Graph for overall Accuracy
#       Updated             20/11/2015
#       Prerequisites - Data obtained from earlier runs collected and initialized
#       Output - Graph for overall Accuracy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['legend.handlelength'] = 0

#Overall Accuracy
x3 = [16866,1500,1000,500,400,200,100]
y3 = [95,96,96,95,95,93,94]

# use pylab to plot x and y
plt.plot(x3, y3, 'b-o',  label = 'Overall Accuracy')

# set axis limits
plt.xlim(0.0, 17000.0)
plt.ylim(90.0, 100.0)

plt.xlabel('x axis - Dictionary Size')
plt.ylabel('y axis - Accuracy')
plt.title('Plot of Dictionary vs. Overall Accuracy of Prediction')

plt.legend(loc='best', numpoints=1)
plt.show()
