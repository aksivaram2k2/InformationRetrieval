#       About - Graph for Model File Size
#       Updated             20/11/2015
#       Prerequisites - Data obtained from earlier runs collected and initialized
#       Output - Graph for Model File Size
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['legend.handlelength'] = 0

#Overall Accuracy
x1 = [16866,1500,1000,500,400,200,100]
y1 = [746,64,42,20,16,8,4]

# use pylab to plot x and y
plt.plot(x1, y1, 'g-*', label = 'Model File Size')

# set axis limits
plt.xlim(0.0, 17000.0)
plt.ylim(1, 800)

plt.xlabel('x axis - Dictionary Size')
plt.ylabel('y axis - Model File Size')
plt.title('Plot of Dictionary vs. Model File Size')

plt.legend(loc='best', numpoints=1)
plt.show()
