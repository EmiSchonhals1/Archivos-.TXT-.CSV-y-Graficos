import pandas as pd
import matplotlib.pyplot as plt   #es una librería para visualizar datos de forma gráfica
import seaborn as sns   #es una librería que nos permite armar gráficos estadísticos

#abrimos el CSV
df = pd.read_csv("Archivos\\Archivos.CSV\\archivo_creado.csv")

#creando el gráfico de barras
sns.barplot(x="Peso",y="Altura",data=df)

#mostrando el gráfico
plt.show()









