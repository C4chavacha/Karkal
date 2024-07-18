import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cargar el archivo CSV
df = pd.read_csv('mundo_ideal_karcal.csv')

# Convertir 'Fecha del Remate' a datetime
df['Fecha del Remate'] = pd.to_datetime(df['Fecha del Remate'])

# Crear gráficos interactivos

# 1. Distribución de montos de garantía (Histograma)
fig1 = px.histogram(df, x='Monto de Garantía', nbins=30, title='Distribución de Montos de Garantía')
fig1.update_layout(xaxis_title='Monto de Garantía', yaxis_title='Frecuencia')

# 2. Número de remates por banco (Gráfico de Barras)
fig2 = px.bar(df['Banco'].value_counts().reset_index(), x='index', y='Banco', title='Número de Remates por Banco', labels={'index': 'Banco', 'Banco': 'Cantidad de Remates'})

# 3. Evolución mensual de remates (Gráfico de Líneas)
monthly_remates = df.set_index('Fecha del Remate').resample('MS').size()
fig3 = go.Figure(data=go.Scatter(x=monthly_remates.index, y=monthly_remates, mode='lines+markers'))
fig3.update_layout(title='Evolución Mensual de Remates', xaxis_title='Fecha', yaxis_title='Cantidad de Remates')

# 4. Distribución de modelos de automóvil (Gráfico de Pastel)
fig4 = px.pie(df['Modelo de Automóvil'].value_counts().reset_index(), names='index', values='Modelo de Automóvil', title='Distribución de Modelos de Automóvil')

# 5. Pagos restantes por categoría de automóvil (Boxplot)
fig5 = px.box(df, x='Categoría de Automóvil', y='Pago del Restante', title='Pagos Restantes por Categoría de Automóvil')
fig5.update_layout(xaxis_title='Categoría de Automóvil', yaxis_title='Pago del Restante')

# Graficos del comportamiento web del cliente

# 1. Cantidad de clicks en "Inicio" (Histograma)
fig6 = px.histogram(df, x='Cantidad de Click en Inicio', nbins=30, title='Cantidad de Clicks en "Inicio"')
fig6.update_layout(xaxis_title='Cantidad de Clicks', yaxis_title='Frecuencia')

# 2. Cantidad de clicks en "Quiénes Somos" (Histograma)
fig7 = px.histogram(df, x='Cantidad de Click en "Quiénes Somos"', nbins=30, title='Cantidad de Clicks en "Quiénes Somos"')
fig7.update_layout(xaxis_title='Cantidad de Clicks', yaxis_title='Frecuencia')

# 3. Cantidad de clicks en "Contacto" (Histograma)
fig8 = px.histogram(df, x='Cantidad de Click en Contacto', nbins=30, title='Cantidad de Clicks en "Contacto"')
fig8.update_layout(xaxis_title='Cantidad de Clicks', yaxis_title='Frecuencia')

# 4. Cantidad de clicks en "Remates Activos" (Gráfico de Líneas)
df['Fecha de Click en Remates Activos'] = pd.date_range(start='2024-01-01', periods=len(df), freq='D')
clicks_remates_activos = df.set_index('Fecha de Click en Remates Activos')['Cantidad de Click en Remates Activos'].resample('MS').sum()
fig9 = go.Figure(data=go.Scatter(x=clicks_remates_activos.index, y=clicks_remates_activos, mode='lines+markers'))
fig9.update_layout(title='Cantidad de Clicks en "Remates Activos"', xaxis_title='Fecha', yaxis_title='Cantidad de Clicks')

# 5. Cantidad de clicks en "Abonar Garantía" (Boxplot)
fig10 = px.box(df, y='Cantidad de Click en Abonar Garantía', title='Cantidad de Clicks en "Abonar Garantía"')
fig10.update_layout(yaxis_title='Cantidad de Clicks')

# Guardar gráficos en HTML
fig1.write_html("distribucion_montos_garantia.html")
fig2.write_html("numero_remates_banco.html")
fig3.write_html("evolucion_mensual_remates.html")
fig4.write_html("distribucion_modelos_automovil.html")
fig5.write_html("pagos_restantes_categoria_automovil.html")
fig6.write_html("clicks_inicio.html")
fig7.write_html("clicks_quienes_somos.html")
fig8.write_html("clicks_contacto.html")
fig9.write_html("clicks_remates_activos.html")
fig10.write_html("clicks_abonar_garantia.html")

print("Gráficos interactivos generados y guardados exitosamente.")
