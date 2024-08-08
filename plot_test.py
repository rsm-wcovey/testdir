import numpy as np
import matplotlib.pyplot as plt

xlist = [1,2,3,4,3,3,3,4,3,3,2,2,1,2,1,4,4,4,3,3]
xArr = np.array(xlist)

plt.hist(xlist)
plt.show()
