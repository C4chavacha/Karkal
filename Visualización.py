import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('mundo_ideal_karcal.csv')

# Graficos de información de la transacción

# 1. Distribución de montos de garantía
plt.figure(figsize=(10, 6))
plt.hist(df['Monto de Garantía'], bins=30, color='blue', edgecolor='black')
plt.title('Distribución de Montos de Garantía')
plt.xlabel('Monto de Garantía')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# 2. Número de remates por banco
plt.figure(figsize=(10, 6))
df['Banco'].value_counts().plot(kind='bar', color='orange')
plt.title('Número de Remates por Banco')
plt.xlabel('Banco')
plt.ylabel('Cantidad de Remates')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 3. Distribución de fechas de remate
plt.figure(figsize=(10, 6))
df['Fecha del Remate'] = pd.to_datetime(df['Fecha del Remate'])
df['Fecha del Remate'].dt.month.value_counts().sort_index().plot(kind='bar', color='green')
plt.title('Distribución de Fechas de Remate')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Remates')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

# 4. Distribución de modelos de automóvil
plt.figure(figsize=(10, 6))
df['Modelo de Automóvil'].value_counts().plot(kind='bar', color='purple')
plt.title('Distribución de Modelos de Automóvil')
plt.xlabel('Modelo de Automóvil')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 5. Pagos restantes por categoría de automóvil
plt.figure(figsize=(10, 6))
df.groupby('Categoría de Automóvil')['Pago del Restante'].sum().plot(kind='bar', color='red')
plt.title('Pagos Restantes por Categoría de Automóvil')
plt.xlabel('Categoría de Automóvil')
plt.ylabel('Total de Pagos Restantes')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Graficos del comportamiento web del cliente

# 1. Cantidad de clicks en "Inicio"
plt.figure(figsize=(10, 6))
plt.hist(df['Cantidad de Click en Inicio'], bins=30, color='blue', edgecolor='black')
plt.title('Cantidad de Clicks en "Inicio"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# 2. Cantidad de clicks en "Quiénes Somos"
plt.figure(figsize=(10, 6))
plt.hist(df['Cantidad de Click en "Quiénes Somos"'], bins=30, color='orange', edgecolor='black')
plt.title('Cantidad de Clicks en "Quiénes Somos"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# 3. Cantidad de clicks en "Contacto"
plt.figure(figsize=(10, 6))
plt.hist(df['Cantidad de Click en Contacto'], bins=30, color='green', edgecolor='black')
plt.title('Cantidad de Clicks en "Contacto"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# 4. Cantidad de clicks en "Remates Activos"
plt.figure(figsize=(10, 6))
plt.hist(df['Cantidad de Click en Remates Activos'], bins=30, color='purple', edgecolor='black')
plt.title('Cantidad de Clicks en "Remates Activos"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# 5. Cantidad de clicks en "Abonar Garantía"
plt.figure(figsize=(10, 6))
plt.hist(df['Cantidad de Click en Abonar Garantía'], bins=30, color='red', edgecolor='black')
plt.title('Cantidad de Clicks en "Abonar Garantía"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
