import matplotlib.pyplot as plt
import numpy as np

# creating the base circle
base = np.linspace(0, 2*np.pi, 100)
x1 = np.cos(base)
y1 = np.sin(base)

# creating the movement path (half circle)
path = np.linspace(0, np.pi, 100)
x2 = np.cos(path)
y2 = np.sin(path)

# plotting
plt.plot(x1, y1, '-')
plt.plot(x2, y2, '-')
plt.axis('equal')

# axis lines
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)

# labels
plt.title("Figure 1- Euler's Identity Visualisation")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.show()
