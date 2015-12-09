#       About - Graph for Testing Time
#       Updated             20/11/2015
#       Prerequisites - Data obtained from earlier runs collected and initialized
#       Output - Graph for Testing Time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['legend.handlelength'] = 0

#Overall Accuracy
x1 = [16866,1500,1000,500,400,200,100]
y1 = [7.05735,5.25826,6.86593,5.67959,8.08867,5.70228,4.88664]

# use pylab to plot x and y
plt.plot(x1, y1, 'g-*', label = 'Testing Time')

# set axis limits
plt.xlim(0.0, 17000.0)
plt.ylim(4,10)

plt.xlabel('x axis - Dictionary Size')
plt.ylabel('y axis - Testing Time')
plt.title('Plot of Dictionary vs. Testing Time')

plt.legend(loc='best', numpoints=1)
plt.show()
