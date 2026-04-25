import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv('Sacramentorealestatetransactions.csv')
tab=pd.crosstab(index=df['calificaciones'], columns='Frecuencia')

plt.figure()
plt.bar(tab.index, tab['Frecuencia'])
plt.title('Distribución de Calificaciones')
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")
plt.show()

aprobados = df[df['calificaciones'] >= 6]['frecuencia'].sum()
reprobados = df[df['calificaciones'] < 6]['frecuencia'].sum()
wdata = np.array([aprobados, reprobados])
plt.figure()
plt.pie(wdata, labels=['Aprobados', 'Reprobados'], autopct='%1.1f%%')
plt.title('Aprobados vs Reprobados')
plt.show()