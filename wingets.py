from ipywidgets import interact, IntSlider, IntProgress
import numpy as np
import matplotlib.pyplot as plt
import time
from IPython.display import display

def myPlot(c):
    x = np.linspace(-5, 5, 100)
    y = c * x**2
    plt.figure(figsize=(6,4))
    plt.plot(x, y, 'r--')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.xlim([-5, 5])
    plt.ylim([-15, 80])
    plt.grid(True)
    plt.show()

interact(myPlot, c=IntSlider(min=1, max=10, step=1, value=5))

progress = IntProgress(description='Loading:', orientation='horizontal')
display(progress)

for i in range(101):
    progress.value = i
    time.sleep(0.05)
