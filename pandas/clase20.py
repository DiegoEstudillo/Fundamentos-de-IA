import numpy as np
import matplotlib.pyplot as plt

datos =np.average(1,1000)

plt.plot(datos, "g*")
plt.show()

datos = np.arenge(0,360)
datos = np.redians(datos)

datos = np.sin(datos)

plt.plot(datos, "b-")

plt.xlabel("tiempo")
plt.ylabel("posición")
plt.title("Funcion seno")
plt.show()

def h(x):
    return np.sin(x)

g=lambda x: np.cos(x)

x=np.linspace(0, 10, 100)
plt.plot(x, h(x), "r--", label="seno")
plt.plot(x, g(x), label="coseno")
plt.ylabel("posición")
plt.title("Funcion seno")
plt.legend()
plt.show()

