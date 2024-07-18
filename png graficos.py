import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurar el estilo de seaborn
sns.set(style='whitegrid', palette='muted')

# Cargar el archivo CSV
df = pd.read_csv('mundo_ideal_karcal.csv')

# Convertir 'Fecha del Remate' a datetime
df['Fecha del Remate'] = pd.to_datetime(df['Fecha del Remate'])

# Función para guardar gráficos
def save_plot(fig, filename):
    fig.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close(fig)

# Graficos de información de la transacción

# 1. Distribución de montos de garantía (Histograma)
fig = plt.figure(figsize=(12, 8))
sns.histplot(df['Monto de Garantía'], bins=30, color='dodgerblue', kde=True)
plt.title('Distribución de Montos de Garantía')
plt.xlabel('Monto de Garantía')
plt.ylabel('Frecuencia')
save_plot(fig, 'distribucion_montos_garantia.png')

# 2. Número de remates por banco (Gráfico de Barras)
fig = plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Banco', palette='viridis', hue='Banco', dodge=False, legend=False)
plt.title('Número de Remates por Banco')
plt.xlabel('Banco')
plt.ylabel('Cantidad de Remates')
plt.xticks(rotation=45, ha='right')
save_plot(fig, 'numero_remates_banco.png')

# 3. Evolución mensual de remates (Gráfico de Líneas)
fig = plt.figure(figsize=(12, 8))
monthly_remates = df.set_index('Fecha del Remate').resample('MS').size()
sns.lineplot(data=monthly_remates, marker='o', color='green')
plt.title('Evolución Mensual de Remates')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de Remates')
save_plot(fig, 'evolucion_mensual_remates.png')

# 4. Distribución de modelos de automóvil (Gráfico de Pastel)
fig = plt.figure(figsize=(12, 8))
df['Modelo de Automóvil'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('viridis', n_colors=len(df['Modelo de Automóvil'].unique())))
plt.title('Distribución de Modelos de Automóvil')
plt.ylabel('')
save_plot(fig, 'distribucion_modelos_automovil.png')

# 5. Pagos restantes por categoría de automóvil (Boxplot)
fig = plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Categoría de Automóvil', y='Pago del Restante', hue='Categoría de Automóvil', palette='muted', legend=False)
plt.title('Pagos Restantes por Categoría de Automóvil')
plt.xlabel('Categoría de Automóvil')
plt.ylabel('Pago del Restante')
plt.xticks(rotation=45, ha='right')
save_plot(fig, 'pagos_restantes_categoria_automovil.png')

# 6. Garantías recibidas por mes (Gráfico de Barras)
fig = plt.figure(figsize=(12, 8))
monthly_garantias = df.set_index('Fecha del Remate').resample('MS')['Monto de Garantía'].sum()
monthly_garantias.plot(kind='bar', color='dodgerblue')
plt.title('Garantías Recibidas por Mes')
plt.xlabel('Fecha')
plt.ylabel('Monto de Garantía')
save_plot(fig, 'garantias_recibidas_mes.png')

# 7. Garantías recibidas por categoría de auto (Gráfico de Barras)
fig = plt.figure(figsize=(12, 8))
sns.barplot(data=df, x='Categoría de Automóvil', y='Monto de Garantía', hue='Categoría de Automóvil', palette='muted', estimator=np.sum, legend=False)
plt.title('Garantías Recibidas por Categoría de Automóvil')
plt.xlabel('Categoría de Automóvil')
plt.ylabel('Monto de Garantía')
plt.xticks(rotation=45, ha='right')
save_plot(fig, 'garantias_recibidas_categoria_automovil.png')

# Graficos del comportamiento web del cliente

# 1. Cantidad de clicks en "Inicio" (Histograma)
fig = plt.figure(figsize=(12, 8))
sns.histplot(df['Cantidad de Click en Inicio'], bins=30, color='dodgerblue', kde=True)
plt.title('Cantidad de Clicks en "Inicio"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
save_plot(fig, 'clicks_inicio.png')

# 2. Cantidad de clicks en "Quiénes Somos" (Histograma)
fig = plt.figure(figsize=(12, 8))
sns.histplot(df['Cantidad de Click en "Quiénes Somos"'], bins=30, color='orange', kde=True)
plt.title('Cantidad de Clicks en "Quiénes Somos"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
save_plot(fig, 'clicks_quienes_somos.png')

# 3. Cantidad de clicks en "Contacto" (Histograma)
fig = plt.figure(figsize=(12, 8))
sns.histplot(df['Cantidad de Click en Contacto'], bins=30, color='green', kde=True)
plt.title('Cantidad de Clicks en "Contacto"')
plt.xlabel('Cantidad de Clicks')
plt.ylabel('Frecuencia')
save_plot(fig, 'clicks_contacto.png')

# 4. Cantidad de clicks en "Remates Activos" (Gráfico de Líneas)
fig = plt.figure(figsize=(12, 8))
df['Fecha de Click en Remates Activos'] = pd.date_range(start='2024-01-01', periods=len(df), freq='D')
clicks_remates_activos = df.set_index('Fecha de Click en Remates Activos')['Cantidad de Click en Remates Activos'].resample('MS').sum()
sns.lineplot(data=clicks_remates_activos, marker='o', color='purple')
plt.title('Cantidad de Clicks en "Remates Activos"')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de Clicks')
save_plot(fig, 'clicks_remates_activos.png')

# 5. Cantidad de clicks en "Abonar Garantía" (Boxplot)
fig = plt.figure(figsize=(12, 8))
sns.boxplot(data=df, y='Cantidad de Click en Abonar Garantía', color='red')
plt.title('Cantidad de Clicks en "Abonar Garantía"')
plt.ylabel('Cantidad de Clicks')
save_plot(fig, 'clicks_abonar_garantia.png')

print("Gráficos generados y guardados exitosamente.")
