#       About - Graph for Training Time
#       Updated             20/11/2015
#       Prerequisites - Data obtained from earlier runs collected and initialized
#       Output - Graph for Training Time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['legend.handlelength'] = 0

#Overall Accuracy
x1 = [16866,1500,1000,500,400,200,100]
y1 = [0.11669,0.00938,0.00707,0.00458,0.01186,0.00243,0.00150]

# use pylab to plot x and y
plt.plot(x1, y1, 'g-*', label = 'Training Time')

# set axis limits
plt.xlim(0.0, 17000.0)
plt.ylim(0.0000, 0.5)

plt.xlabel('x axis - Dictionary Size')
plt.ylabel('y axis - Training Time')
plt.title('Plot of Dictionary vs. Training Time')

plt.legend(loc='best', numpoints=1)
plt.show()
