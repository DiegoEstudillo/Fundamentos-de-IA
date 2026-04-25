import pandas as pd
import matplotlib.pyplot as plt

df_profesores= pd.DataFrame({
    'Nombre': ['Jaime', 'Armando', 'Oscar'],
    'Apellido_paterno': ['Minor', 'Alvarez', 'Gomez'],
    'Apellido_materno': ['Gomez', 'Galvan', 'Sanchez'],
})

print(df_profesores)
print(type(df_profesores))

df_archivo = pd.read_csv('Sacramentorealestatetransactions.csv')

print(df_archivo)

print(df_archivo.head())

print(df_archivo.head(20))

print(df_archivo.tail())

print(df_archivo.dtypes)

print(df_archivo.describe())

print(df_archivo.loc[100])

print(df_archivo["city"])

print(df_archivo["city"]=="Sacramento")

city="Sacramento"

print(df_archivo.query('city == @city'))

#Mas registros (ciudad)
print(df_archivo['city'].value_counts())

#Ciudad con mas elementos
print(df_archivo['city'].value_counts().idxmax())

#Registors totales de la ciudad
print(df_archivo['city'].value_counts().max())

#Promedio de precio por ciudad
print(df_archivo.groupby('city')['price'].mean().sort_values(ascending=False))

print(df_archivo.to.excel('Sacramentorealestatetransactions.xlsx'))

print(df_archivo.query("city == 'SACRAMENTO' and price > 300000 and price < 400000"))

conteo_ciudades = df_archivo['city'].value_counts().head(10)

plt.figure()
conteo_ciudades.plot(kind='bar')
plt.title('Top 10 Ciudades con más propiedades')
plt.xlabel("Ciudad")
plt.ylabel("Cantidad")
plt.show()

plt.figure()
df_archivo['price'].hist()
plt.title('Distribución de Precios')
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.show()

df_archivo['city'].value_counts().plot(kind='bar')
plt.title('Top 10 ciudades con más propiedades')
plt.xlabel("Ciudad")
plt.ylabel("Cantidad")
plt.show()

precio_promedio = df_archivo.groupby('city')['price'].mean().sort_values(ascending=False).head(10)
plt.figure()
precio_promedio.plot(kind='bar')
plt.title('Precio Promedio por Ciudad(Top 10)')
plt.xlabel("Ciudad")
plt.ylabel("Precio Promedio")
plt.show()

