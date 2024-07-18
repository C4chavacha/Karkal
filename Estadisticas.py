import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Configurar el estilo de matplotlib
plt.style.use('ggplot')

# Cargar el archivo CSV
df = pd.read_csv('mundo_ideal_karcal.csv')

# Convertir 'Fecha del Remate' a datetime
df['Fecha del Remate'] = pd.to_datetime(df['Fecha del Remate'])

# Crear una columna 'Cliente' combinando 'Nombre' y 'Apellido'
df['Cliente'] = df['Nombre'] + ' ' + df['Apellido']

# Calcular estadísticas clave
total_clientes = df['Cliente'].nunique()
monto_acumulado_garantia = df['Monto de Garantía'].sum()
autos_por_categoria = df['Categoría de Automóvil'].value_counts().to_dict()

# Estadísticas adicionales
promedio_monto_garantia = df['Monto de Garantía'].mean()
mediana_pago_restante = df['Pago del Restante'].median()
cantidad_remates_mes = df['Fecha del Remate'].dt.to_period('M').value_counts().sort_index().to_dict()
cantidad_remates_mes = {str(k): v for k, v in cantidad_remates_mes.items()}  # Convertir Period a str
max_monto_garantia = df['Monto de Garantía'].max()
min_monto_garantia = df['Monto de Garantía'].min()
total_remates = len(df)
max_pago_restante = df['Pago del Restante'].max()
min_pago_restante = df['Pago del Restante'].min()
total_monto_pago_restante = df['Pago del Restante'].sum()

# Indicadores adicionales
if 'Cotizaciones' in df.columns:
    autos_mas_cotizados = df.groupby('Modelo de Automóvil')['Cotizaciones'].sum().nlargest(5).to_dict()
else:
    autos_mas_cotizados = {}

if 'Visitas' in df.columns:
    autos_mas_visitados = df.groupby('Modelo de Automóvil')['Visitas'].sum().nlargest(5).to_dict()
else:
    autos_mas_visitados = {}

if 'Garantías' in df.columns:
    remates_mas_garantias = df.groupby('Fecha del Remate')['Garantías'].sum().nlargest(5).to_dict()
else:
    remates_mas_garantias = {}

clientes_mas_remates = df['Cliente'].value_counts().nlargest(5).to_dict()
categorias_mas_remates = df['Categoría de Automóvil'].value_counts().nlargest(5).to_dict()

# Guardar las estadísticas clave en un archivo JSON para usarlas en HTML
stats = {
    "total_clientes": total_clientes,
    "monto_acumulado_garantia": monto_acumulado_garantia,
    "autos_por_categoria": autos_por_categoria,
    "promedio_monto_garantia": promedio_monto_garantia,
    "mediana_pago_restante": mediana_pago_restante,
    "cantidad_remates_mes": cantidad_remates_mes,
    "max_monto_garantia": max_monto_garantia,
    "min_monto_garantia": min_monto_garantia,
    "total_remates": total_remates,
    "max_pago_restante": max_pago_restante,
    "min_pago_restante": min_pago_restante,
    "total_monto_pago_restante": total_monto_pago_restante,
    "autos_mas_cotizados": autos_mas_cotizados,
    "autos_mas_visitados": autos_mas_visitados,
    "remates_mas_garantias": remates_mas_garantias,
    "clientes_mas_remates": clientes_mas_remates,
    "categorias_mas_remates": categorias_mas_remates
}

with open('stats.json', 'w') as f:
    json.dump(stats, f)

print("Gráficos generados y guardados exitosamente.")
