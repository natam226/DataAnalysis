#Análisis para Corte 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

zaga = pd.read_excel("dataset\Radicaciones y pagos.xlsx")
zaga.head(10)
zaga.describe()

advisor_counts = zaga['ASESOR'].value_counts()
advisor_counts.nlargest(30).plot(kind="bar", figsize=(10, 5))
plt.grid(True)
plt.title("Rendimiento de los asesores")
plt.ylabel("Cantidad de clientes")
plt.xlabel("Asesores")
plt.yscale('linear')
plt.yticks(range(0, advisor_counts.max() + 1, 1))
plt.tick_params(axis='y', which='both', left=False)
plt.show()

colores_divergentes = sns.color_palette("viridis")
zaga.CONVENIO.value_counts().nlargest(20).plot(kind = 'bar', figsize = (10, 5), color = colores_divergentes)
plt.grid(True)
plt.title("Rendimiento del convenio")
plt.ylabel("Cantidad de clientes")
plt.xlabel("Convenios");

from matplotlib.ticker import FuncFormatter

zaga_sin_negados = zaga[zaga['ESTADO'] != 'Negado']
rendimiento_asesores = zaga_sin_negados.groupby('ASESOR')['MONTO '].sum()
def millones_formatter(x, pos):
    return f'${x / 1e6:.1f}M'

plt.figure(figsize=(20, 10))
rendimiento_asesores_sorted = rendimiento_asesores.sort_values()
colores_divergentes = sns.color_palette("coolwarm", n_colors=len(rendimiento_asesores_sorted))
rendimiento_asesores.plot(kind='bar', color = colores_divergentes)
plt.title('Rendimiento de Asesores por Monto Prestado')
plt.xlabel('Asesor')
plt.ylabel('Monto Prestado (en millones)')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(FuncFormatter(millones_formatter))
plt.tight_layout()
plt.grid(True)
plt.show()

zaga.ESTADO.value_counts().nlargest(20).plot(kind = 'pie', figsize = (10, 10), autopct='%1.1f%%', fontsize = 10)
plt.title("Estado de los créditos")
plt.show()