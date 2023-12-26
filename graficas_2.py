import pandas as pd

# Datos proporcionados
data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

import matplotlib.pyplot as plt

# Crear el boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df['nota'])
plt.title('Distribución de Notas de Estudiantes')
plt.xlabel('Notas')
plt.ylabel('Valor')

# Mostrar el gráfico
plt.show()


#import matplotlib.pyplot as plt

# Contar la cantidad de estudiantes aprobados y no aprobados
aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

# Etiquetas y valores para el pie chart
etiquetas = ['Aprobados', 'No Aprobados']
valores = [aprobados, no_aprobados]

# Crear el pie chart
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
plt.title('Proporción de Estudiantes Aprobados y No Aprobados')

# Mostrar el gráfico
plt.show()


