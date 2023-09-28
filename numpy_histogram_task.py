import numpy as np
import matplotlib.pyplot as plt
# using random numbers
a=np.random.random((3,5))
print(a)
print(a*100)
plt.hist(a * 100)
plt.show()

# using normal method
x=np.array([[1,2,3,4,3,4,2,4],[6,7,3,1,2,4,1,4]])
print(x)
plt.hist(x)
plt.show()